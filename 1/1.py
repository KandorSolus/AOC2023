f = open("1.txt", "r")
num_words = {"one":"1ne", "two":"2wo", "three":"3hree", "four":"4our", "five":"5ive", "six":"6ix", "seven":"7even", "eight":"8ight", "nine":"9ine"}
def replace_words(text):
    testi = " "
    testj = " "
    idx = len(text)
    while testi != "" and testj != "":
        testi = " "
        testj = " "
        idx = len(text)
        for i, j in num_words.items():
            if text.find(i) < idx and text.find(i) >= 0:
                idx = text.find(i)
                testi = i
                testj = j
        if testi == " ":
            testi = ""
            testj = ""
        else:
            text = text.replace(testi, testj)
    return text
nums = [replace_words(line) for line in f.readlines()]
nums = [int(''.join(filter(str.isdigit, line))) for line in nums if len(''.join(filter(str.isdigit, line)))]
nums = [int(str(num)[::len(str(num))-1]) if len(str(num)) > 2 else num for num in nums]
nums = [int(str(num) + str(num)) if len(str(num)) == 1 else num for num in nums]
print(sum(nums))