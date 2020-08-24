from string import Template


# 從標準程式庫的string 模組匯入Template程式碼。這樣就有簡單的字串替換模板可用。

def start_response(resp='text/html'):
    # 用於建立CGI的Content-type(預設為 text/html)
    return ('Content_type: ' + resp + '\n\n')


def include_header(the_title):
    # 此葉面本身被存放在 templates/header.html 這個獨立的檔案中，而且會依需要替換title

    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return (header.substitute(title=the_title))


def include_footer(the_links):
    """
    類似 include_header函式，此函式也具有一個字串引述，用於建立一個HTML頁面的結尾。
    此頁面本身被存放在 templates/footer.html 這個獨立檔案中，引述可用於動態建立一組HTML連結標記。
    根據他們的使用方式，看起來引數必需是一個字典。

    :param the_links:
    :return:
    """

    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return (footer.substitute(links=link_string))


def start_form(the_url, form_type="POST"):
    """
    此函式會回傳一個 HTML 表單的開頭，並讓呼叫者指定用於傳送表單資料的URL以及所使用方式(GET or POST)
    :param the_url:
    :param form_type:
    :return:
    """
    return ('<form action="' + the_url + '" method="' + form_type + '">')


def end_form(submit_msg="Submit"):
    """
    此函式所回傳的HTML標記，可用於終止表單並允許呼叫者自行定義表單之submit按鈕的文字
    :param submit_msg: submit按鈕的文字
    :return:
    """
    return ('<p></p><input type=submit value="' + submit_msg + '"></form>')



def radio_button(rb_name, rb_value):
    """
    提供一個單選按鈕的名稱與值
    以便建立一個HTML單選鈕(他通常被包含在一個HTML表單裡)
    注意:這兩個引數是必要的

    """
    return ('<input type="radio" name="' + rb_name + '" value="' +
            rb_value + '"> ' + rb_value + '<br />')


def u_list(items):
    """
    提供一個項目清單，此函式會將該清單轉換成一個 HTML 無編號列表(unnumbered list)。
    一個簡單的for 迴圈足已完成此工作，每次迭代會將一個LI加入UL元素
    :param items:
    :return:
    """
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return (u_string)


def header(header_text, header_level=2):
    """
    建立和回傳一個HTML標頭標記(H1,H2..)，預設回H2
    :param header_text: 必要引數
    :param header_level:
    :return:
    """
    return ('<h' + str(header_level) + '>' + header_text +
            '</h' + str(header_level) + '>')


def para(para_text):
    """
    以HTML段落刮住一段文字(一個字串)
    :param para_text:
    :return:
    """
    return '<p>' + para_text + '</p>'

