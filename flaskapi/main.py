from flask import Flask,request
from flask_cors import CORS
import seamcarve2
import time
app = Flask(__name__)
CORS(app)



@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    # time.sleep(10)
    return "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gKgSUNDX1BST0ZJTEUAAQEAAAKQbGNtcwQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwQVBQTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLWxjbXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtkZXNjAAABCAAAADhjcHJ0AAABQAAAAE53dHB0AAABkAAAABRjaGFkAAABpAAAACxyWFlaAAAB0AAAABRiWFlaAAAB5AAAABRnWFlaAAAB+AAAABRyVFJDAAACDAAAACBnVFJDAAACLAAAACBiVFJDAAACTAAAACBjaHJtAAACbAAAACRtbHVjAAAAAAAAAAEAAAAMZW5VUwAAABwAAAAcAHMAUgBHAEIAIABiAHUAaQBsAHQALQBpAG4AAG1sdWMAAAAAAAAAAQAAAAxlblVTAAAAMgAAABwATgBvACAAYwBvAHAAeQByAGkAZwBoAHQALAAgAHUAcwBlACAAZgByAGUAZQBsAHkAAAAAWFlaIAAAAAAAAPbWAAEAAAAA0y1zZjMyAAAAAAABDEoAAAXj///zKgAAB5sAAP2H///7ov///aMAAAPYAADAlFhZWiAAAAAAAABvlAAAOO4AAAOQWFlaIAAAAAAAACSdAAAPgwAAtr5YWVogAAAAAAAAYqUAALeQAAAY3nBhcmEAAAAAAAMAAAACZmYAAPKnAAANWQAAE9AAAApbcGFyYQAAAAAAAwAAAAJmZgAA8qcAAA1ZAAAT0AAACltwYXJhAAAAAAADAAAAAmZmAADypwAADVkAABPQAAAKW2Nocm0AAAAAAAMAAAAAo9cAAFR7AABMzQAAmZoAACZmAAAPXP/bAEMABQMEBAQDBQQEBAUFBQYHDAgHBwcHDwsLCQwRDxISEQ8RERMWHBcTFBoVEREYIRgaHR0fHx8TFyIkIh4kHB4fHv/bAEMBBQUFBwYHDggIDh4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHv/CABEIAZABkAMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAADBAIFAAEGBwj/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/2gAMAwEAAhADEAAAAfMxT0iSraYwyjNVZV9hXRWRlrRbhKJM21HIqvINilcyhKXYWFfY5aF3mppogpyxAINknEnW+yQsKJQi2nYIKEiQqwizGknIEobmNxrz7mmldpZKJkU1ZQDNw2zeaxBoyxzFFpMeEGZW9XvV8vW9ZUyhuLRG02paNig61ZyhOKs3U3Mdi6job2x7kDDem5WFbai63m77myY2Ve8jdZY01JVpVm4NOE08FKptcQsWGksMrNAvrWmslGSMzNAzGcXKIoyHswWJ0Ok4mKOt5SyMoik0ueWnaVdqJwwWIuxZXYz13HIod2HQ8yOJzuqPoibOgtalDB4aFKlt6K5kwA1I29YGcx1/m9KtmI+kSaGMcM1tre47CUZaBsBqskBRzKmwuzNyUZWc5mRFLWaYQo8lhuaa+QVlZqKdYAaNda1gj6hg95rSo/T8v1aSqJnMmOFunN1tPYVnVzNEjJhszQS8y7vgrkDAT6SwFhdGs1tmZmBvM0F/zfsvMZvzuXWc+xRlViqkvZxlVmWemq3TajC63AB9HzvSSY2s1noyQcpvNwuk6rOm5mXmM2c1W9bLOfVrfLWHH2trWND18VeqWPfwsbzBl3CbOZ5S5pNImQbFIgJjDN62zMzAzN6Dskq1PJ29Fg6Yd5CyeQxKW47EyvmAUJgj30lB0UvTAWMtG878/B28lxvqHiu+fqa3BdeV0L9C3xdLlmKfLsn0y7vXx8TX7F6PDXFAxczkMgEmNFrhlih0k7CzFoWt7CO82Gs3sIyjIGVSLo3gdMyEthHeaCUcwJZHALkdJt9BTXedSOI2ena0UkOLszmJP9WK3XvXvJsjdnb49lniNTiLmunrtcvNdu1/q86TM2tJQLCaJ0N7yNKjEUeskOPYtSjtm8zYayWwhveBMPXo5VzQrlOlXyYHSHk4hmQxk9ZsNZuKDu1MQ6N/jrKL9Jr2bDzO5iUueTdMbIv0GlrOWeXqr3zX65rjfgLyPB2dZ5v2/LehyqtIz7ecexllz897bhLQMiTWDit7iTkt9hIfHb7BRrmss69rWawPQ4jly9GoE2Cq9jJnPKdmVrz1H06DXlsfSVXPnsvSL3DfyGPtW8tfELf1fi7lCx5bo0VB9Vm+PVdXwHdc3R1XkHvPB5nkPpy6dr0HVclydD9R0/m++BjcM96XF1JeeeQHlrWmoDKcqnMloNSjpk2UpIvX+V2HV5ykk+/3vfNvGBos0bRkx7kIc9qFx0NZqQ5Ot2S+ZbslTVcS86ued9DiYcTnrlf2fKN53rt+L7GH6Hz74+TWvS6dzTPk6S2K31Hl3p3kl4cGKWevxwlqCDantMcT4AtzweThiCbDgHwGATcdp+jkNrn6N6zUEow0wimIYbsvwny9Z9iZHMNhTqQ1Z0OjGlSNnby4xgwbs69yafWasorXecPfSrXOcJISzXusNLTzX0TnHl4vW+uh9Ln8lj6ehS4LXbV1Lm8sVKke96CexbTLgsAsdbS1om2/RyFhy9G4CwNBfrJdc+Fjj7Wq1uAV3R0djU2FI1SOdImq+jJgJZVDAsmwO9DZJidrlQ5zpRdPYVPR42e3Ss8rvOV7Dkqw5yMi9sQ2GKGMUm1MMd2lFLeaXLpdw0PzRT1Zdnl8fSFqXnuu1Q0ntWJp8PTXsGDSLS9Cpy9NdjCE2eM16TSx5VCkJJ3Ncrfg0mpPFioFNuMvM0yqX6SolnXWLpW+b4n0GAenm6Sw4rsqzNz15zHLvT5PfZmHRAhKORYIT6zUNRhSMVUsjeB3N73LUhTA2UYRg5Wm1Wt4dFskyrjpXKNIbZ2Id1bhmAD6TohAlRXdqCFjLn2h6YnYqa9lkOvskyDK8nY5U+m5cVNTfePez7YXnE9l58ZiOnPaiJsjDUNEDUDaFHISDYXBjDsZmtbyU1sRcCkGhHk7LSx5t9HVL184oNFZ1W+W14C2zsrSoss6jXbRY8ngKnGlCUrF9BvO7OYGM2KMxA7tWwTlep28nnfrPk3r23I1553vn9ocTQuh6nsBEJocyRkCgrNVyOepjXhYAFoUyDDM8B0FB0nNzcbKpajS50DMtIolBpmtDWtIbIoxLxQoWh7DlyYyrcuxdrH4uxnXAzdqJN5mmkiB0PQ8FYQoencT2WmNJzLqmpkJwalIkEazMGXBmdTDNZSSQiUt5IaIDYxgpbbmuZ5foOfpQ3vUbNkTLDOuZdicM1eR2lmhyAbJuumyGoHgGmn3qgUXeu8x1MsE5TlkgQiUGR9CNxk/K3kGWR1kuRxAzAaAO5wYfU4zQyDYcr7wgsFPYQ0XQ1zbgnyKpxaxXFXLnrOejRcBEE1XkAW4ZMIyZyaNNLLOLBVycjUNnB02d8tfmnNLt4ySHRCscuqXoM2vR3/P74x3mWTiaIAZAdIe4FHIoMTa0rpMwiwqZbjEW562PIbGjiaEtd1YMPzWw3cmi9GgVnUGkyqm1zs3VW87OQEJCSxSaWDJS1fdbyHVZWxg2EgrzHcCUBz1HVdZ5T0+Ovc0nQ0d5gKKe2chF2nOS8kMRFoDTGVuEhsy9RYGhYgyXOo62G46lNeNFXL3c10JXXNrK+53qIoC9opnrSDsRXA21sCzqzxqZFSYRJfJq3ekp+oxtB+iF0YdFNB0KzhPUOWmkvQuQ6/DbrOH73hawDvetkWQdpxmA7CALNA54cIwySbQEm1QYFDcFkGYZmRR5BCce3mhmYGdjx15jr0qu1+XpiBkLS+x5UlWeCwRklHndmX1GvQdDzPTc+nPLGW7eZq+5q+Q/Q22oviut5e1y19Z43o6Kc0MIDokk4GTSi0MmOi6oGbCyylTYK1ETaIqkgAijnU7yE5PHoyj280dT03FkEUdqEm+DtlW2Y2udjXa6ua+BV41MGQuOieqei5Om4uMf49/LjKIelydNacc+jsSUTEVpG4oM9PW1J9DgcIrYodEDdWKNQoiUpE03FJMzWG0IJXIym0qVMA7FhuJ1JNTFJ5cr1VN04V0Z5QPJ4HU3PBdfydN3zznHOa2JYdvNqY9hMc9IP1nFXuGvodhQdB53YLjPS3BeB5c03qcRnaqLXRF5eUX6l6Z436x5+5Od7WFc3mJb2g31EAy1J5yvsJotc8jNB04SpLtQ02i0ItKK8jCiIkBcuIpNJWr7nbnmkOxrqXNYxDSR4SaFIuyZVwshtJzZwSeMrh2vW+R9dw9foV3ye+Tc/nvRVffyUanTy1jiAdwpU03rHnCOWv0K94N1PFp6VxSru8qLtV2s2QhFQxgyxYmQbaNDClQjIqYCxOkjMganlTazSYTjIUJxMOppexVpczGzSqR6NEAiYG0Le9ikaFkmvWdVXql3jZLMPcg3Le5cHoPBaqPsp8g30mgXE2AZq22XkSfjMa0GMFhQDAjcYonCBFUWD6GgJmDn//EACsQAAICAQMEAgICAgMBAAAAAAECAAMRBBIhBRAiMRMyIEEjMwYUJDBCFf/aAAgBAQABBQIRp+rYIJd/T+B7U/WUDN0Ep9L3T0Y/emdM4TXNmwnmqGahvGw8rB7hlSl369b83WH9pAMm8+f45hgPFx5EE1H1/A9k/qml/v7VRO6wxu9U0njRqT/IPdfr/wBak+RPmvodjNIQjsxaf+19Uf2k5J/IzPDHJEE1Xr8D29UTQf3QSv0vdYY0Har2PHTWHlPY9JLjysHpexmuf4ukNF9yvir8sQxzhYIv21f4/uNxTNGOy+0g7D2ITGgg+2m5s1B20OZXCcDOK7zwvYd/8gfboXMTs/FX4ns0tMEEr++q9/h+5b9Jov6xE9pB2HsGEw9l96EZt1zeL+qhHMt4r1Bie/33/wAjfPUbIsHJu+5/NvTHkehK/wCzU/b8B7Hu/tpP6pVEghiwGZ7rOnDLa0+Te6/TffUGWnL1z99tON1utt+fVt9llH9jHJ7j8L2AEHqUf26n7fgIv2vPbT/0yuLBDF/FJ071qWzb7ZPS/e8+R5ZPQ7u/w6b0P/Ur4r/MiWjyn6E0/wDZqP7PwET7We/1UP45XF7NF/GuaTilzl6NK7QipEuCy08j2PQ7D31h9nTGMTs3FX56npmv062Agz9TT/2Xjz/Gv7WfaL6iQf8ARSJSCaNPp66zdCvyG9staeEn6Hfrz+bxYJd9vz1mstc6t1LNVpmmqVUulL/G51CNM6Zp8VLQ6aNRYO1Xt/uPsIPawd6NBY41PTVFcavz0/T2eaXQ6Sapba1XVuDU12oN4Gko/wDNsSGL2Ayeq2fJ1F/ayofyMcn821yFr76mbcpmp/u/EEiC60Rjk1Q+6xm2CLEqsZdrZr6c4rPUdSD0jqnyjqHwafW0DJ1NWbFpes5ISjp9LajcqV9Rs33ufCyVwxYIjBSx3T9yr6/9DR+xGSRMdszP4V9tNzfiCV/aq1FqXUITqLlFbY3aOzbYWbWV6u/UKvT79Zc91jWJp6nU1+c1gT/Wv/usPi/tPRg7dSf4+nGL29Vf9DPGMzMx/czMzjttmIuYZox/yIIu0woiaDVa2pbOoN82lHT7BK00lJ0NFmtF1StZpqttfwiIsCYnU94r/dvo+19Hv1t/439L2s9/9Bh7Z7YmPyDGZmg5t7KJpwz19QoUs+nmgoRNVVp9NU2hYaWnQ6TGn02GC8kJiOeNTSt9Wp0tunsulNT2W2020hhhh26q2/X3RYgy5OT/ANDKRGhEI/6Md6rWqi60xddVK9VS0ocDTMVuuOgHw1U1azRL8zLpNxRLFGj6ZbhUetWN1RW/U0CUahLJ1BFu0N3tyu2q60aa05eL9nffY/JlYOP+k08PosyzS2LCpWFRNk2GYPbP4GH126eN+pW4M9C7Q2tX/X0epsqdLUsalc31h51LqBoI19jP0G9b7NXpaAoqb5qv7NTXUrgoDkYgmsf49H6X9zQ6y3SAdXDQarpFk/1+h2w9GoeP0TWiXdP1tUKle4xCBMT44dNUY+hoMs6eI3TrhG0uoEesibJsmDNrQUWmGhxPieaNWpNVwQnqTfHdr9QDT1ByuntAfReV71+GoRmtSh/k6SzaHT6KxtRNWUps6ezXa3qq41C/bv1dv+M44xjtn8BxEvuWVdU1yQdauI/3un2wp0a2Zz3DbZugyYvHbiYqjaTTvD0uiVdKpMXS6YBVrExWY1dJnWnXKgzT7Hms0TYWh0GjVlTo679RcgNLUValtVVXpGq3W26fUFU1FgnSKvH/ACp7KOpr1DUrF6q8XqdMTXaVp1XUBr/kM3CeEws2TaZzMzP4rx2MxAOZ+oTgkytQxGxJvivMkzAxrNR8dbuXs9FPVGpYAW0YJIu6OVBd8IKZqtCuolHTPiN++mqjSX3W6Ndif5lSG1zIFmVgG4suJiY/AcQM03mbgZ4GbVmwzDCZMXMPYcRRFhTtnlcE71RFXdNs24hwsut46nadgiweM+0oWatcTpTI1FFldi0nbTpj8rar+Ku9dZqHqRkmlDT/ADBs9Q+WwT5bIWYzPIP44mJiY/Dc03nsFhM8cECDtYecWk1qomBC+JVuc3YRndCb28tW2517KpMVVEq2MrV7g1N1Y6Ivy27sJpOH1tnyuzZmm0wzWML/AJXU1l9mlebBNsCQqROZmZmZmA/hiYmJtg8STyCFJYTcJul1qqqEk7gFNyBajule3Ne2an+yx+bDgOCzKuDzEQsQUEqsYFbkaVNiIzrZWzbL9UCUtbNO0mthKn56pj53HL0UvH6bp3j9ISf/AC1K3dOtWNp7VhWbJtm0zHbMzN0yO2/MGybkgAc2IBLEKptew6dQITmamU2qjad1YMyob72Lvdk2sYPTCV4KOYhxCYMiI7pK9bqdv+5fZKTmVWMBQcSgsDQnHV8G+biCTuJsIiuMuqzAhqRg2h07R+m0mP0to2gvEfS3rDXibJtmDDMWbSBt24i75g41xYIisFVcE2YE2ZattoeyXDdPjWpXbLZ8EGRzkpxZWwC5ylZY16IyzSOBbZdS/Tr6r5XVKqlsNCN8gOK+pgCzPLKCBxCpnIln18puMzN0DQMDCitGqEbS6do3TtM0fpM/+XdNrkDbtsVs1g4Z8S/zchgiTIleBLuFqfJuAzZ41tvtNlZWAZA9beQYkdAZWxVtNZwiqRdpVddX00oNK27T6Z/9ilRuVmnUB/O6kGYBjeiMgAZY4MxwGxMgxDCSJvbGMnfiZImYTtUi0ziFtxq01bLqVVG1PIQb22qobcrPgpQcJqbkIVd0ChTq1xWOAozAI1c2lSpBmwMoBWaXUStwxtrc1rbYydGW+g6d/wDjUpmzXt/Kx4SOBjAm2EGfZWrnKz3BtgyJnMUz12GMCGHEsfJo+LFe0HU7d12SqcSmszVP5IW2u5UbNoswgqVQNWczMT2PSg52ZjLiVtg8RqsxKXC6Wx8XA6XWaa6mIjvFHx1auwWMNoP6si5ycg5Ofc5xmbFM2KZZWFdQMsvI9TaJ+9N8bpqVNXZauKyxF6w+sgN/sDa1xLtZzUplILG1t99jIFuPIi+1iDlI4EK8qCIxIFN/8VAX5dfpk1XTqdRqrdP0kltJqWYaZz5ljA8LAxssxGFSfYt2VsTOZZlhmK3B4nuDMPM5dd4gPNFgJD7peVl2Nje2sCpX7RcsxADuMAsbN20MeySv2hxEGYR2PBzuRF8agwey4ro6kVa+mKf9bVeOmYfyY57YxOZiACFfAiERfqOQyYIEHqZgM0Z8r2JdSTKhBdGfdGJxZ9nMBlDfyW2LCZk53QnyzE91xTyhMBzDMgxTtNLBjpRhwivSTt0/SwRpepEDTHO7PP6nuMBt7eowGNsEHv3MYhJxVtcMggTM6hQGNkXIlVsNizPBYSwGNjC8kYhbMY8FjndCYOYvBq5icRbFADq0xmWAmBsyktWNNqlC6a+tpfp8XaPjS9Qu32HgsOf1jgRgIIo5EONu4Tj8CJjaQGLMNQJqM/G5gicgbduTgkCN6eLF9iOuY/r9mCKYkVoxhzlXeVElvhxcpYMMkUWFXo89Tu2abVtusbmMfFeTjxhiDKnIbHFamWKu7AgPJEzMtPZDYaW2ZVz58xYpOcxox8c85ixe1o8QOSJ6i8mpZlRAwMC5BJBJ2z/zjcpiLumgo51t2IAd2cMcFSMFj5H3jhOWX0CwjM09q1YJCYg9HmDIm7PaoxpqhtdeZiKeBBH4h7LFmMs4nxRhgDkgQNiPa5KbjNJ9GT/lakZi52r4qBumlpEdvjputJfd548k5h+ss9jh/wD2w8yNpMQTlWPPY8z9bJshEYlm1Chq0OABzjExFPN0/cURfdY5YQAk3iGLvJqoyLKPGpcOp8a87rBPQHJ01WJV5HqDjLjc23aScODxj+MT3H9vyvtAVZSi4+qs2Z+8cfr1BCwgMeE8MVD5zFbt7hMPvMWKJWI4ithXXgLC4Wad2zUA6tpwr7IqTHGOEwsFmZpVzOr1gBmwlnMAxFOXuxlIV8z6TgIeM7YDkEZKDjHMzzAcQmeoxAGo1BY1rgVtDzN3DnEZuCeauSkAiSzmBYcLLbMypOaVIbSpLh/IqxyFhbM37Zddkaa7DabXrNezWIw8W5VZnDv9kXADZbI254H2xFHOInLPwR7xx+hzOIyzVXbiBl+MP7RsRlhHFiQjmo4KxYTgC3dN3Fu0yxplhNFcBK9Qu1Tkcy1CSqTVk0y2+VXNnpqsz3IV0L/VvSfXBlojnBH2Jwucwcq3M3ReYvFj8wRZnzM9xTMyv7CXCIPKsfxMsdeLE524KNEMPK52FXGM04ayvCspNNStKaNlaP5tcDCYs6pT8ulFDmaXRzpVNdU1aBtFcfE+lyqp9duS5yycxv6opwDzK0DNnY9uI7eT8PmE5mfGHkxDifNifNkVvutq5VhGHDrCsIgiMRLMGKoy1KT4hBXzpFINx/4tedyuRKnyueMZF9fx2UHy0Z5Xyo1An6XhW4ljeA9LwpOK2dTCPJeYvi7LuirfWykMuNyfoQHjifvsey8NpWBSMI45YT9AQrGBB/SFWmxRK/dGdzr/AMVB/HKzgryo4HU18abDnp9+G0jbq9QPMjwrO6PEVWr2EDnbnKiBnVUbEs+6RDmYKFURQeD2xyfx/eht89+I7zOQ5mYreRjembEFnkLcqtvOnshb/hu2Kv2DNISwLbiwWxHq+GzSNOmHw13FpOEHv2wGQyMq7hhVIHiAoDwaZnTDqyttZSQbjmEwjKxeADPf4iaVtt4jrEAM1Y2TfPkwVtzHuxLLMwHJQBkoq3GrT7QFZtJdZ/Il5lTBitxRUtUqJ1JZpj5dOHh1erbYMCYw31tEy+5FBcL5bQWUBbP5Fe6zLYzDPa/quOuDkzEXiH8PXavlMbpWrb+o1MNMTN0zDMQTQvNP9qea1OB1So061WIldmImplNqNEdg1hW6qk7X6S/yVamj5tO9fkvB9yn7WcWZG7dixmT5gNssOD9hpzyQMlfEys4N44MCn45dWUP4GdJb5KtMoEWr+XrV4Ws9hM96W22UsDNK/j9n6h01NfOq9KfRL2RyGTVukXWAtcyl+hXsllNoZdToq7n1PTbE7J7vYfIDht/gq7gy4a7605dlLfJZ6X6ftYxxZtO6k4BllYcW0FYR+FN1lM0+sq+O7rFQbU2tfaYfy0F3GkbxqBMqsXHxq69Y0n+nr+xM3yu7a3RNRsupZN2e3VdNstr96v7j6gcK2EZuPZATNjYKsMKeGXlTtFx3TPgqliQY3rZmfAmw6Nc2aUiOu04mJiGGEQ9h3VtjaC/K6a3yXAtp5n+S6VHR9PXh9K0sptEIMM0erNZ6Trwy06oGb+eokPoQOdXKzyCMZMoOYf7X4YMLahX4nxnuOPACKPEeLZ5gXcWOexmp0+RYhVpibZsgVY1YmwTasKQpGUzT2tS2k1asOnatbEfqaVV63qFmqpQ5GMNV7srVi2grY6npFixLrtM1PUMxOtiuijW2XVpymqH8KfYQHER458n/ALEXJqLLLByvqzmtYZdHHIjjakPr9jmX0AzZ5Y7CGLkmDtiVoDF0a2u2ldXrquIqpRY0RfP9odpAirzRXvS7R0ur9F0plHTq0LIq1r4mxdy/GVKAkqExcB8jiIA0oNYexNsQ5hq5IICjk8BeUeUjLEl3ImMQrPQK+LaYbbKG3NW4IVhGg9kdgIBkoMSnhYPX7lf3x4pAvIHlVlSRla+Vt+xxkjK1cq1TiILlPO4jMsHiMQDHbHAyIzOTX7cyziW8T//EACURAAICAgICAgMBAQEAAAAAAAABAhEQIAMSITEwQQQTIhQjYf/aAAgBAwEBPwHC1WFu9HshaIWFu/iWXohaM+sP4WRw9UfReWKDl6J8Eoqx/D1FmtlDt6HBxFBsh+O37IVE/J5e3hH3l7XuhKz/AD+PZyf8/RGXZeTjxyyHo/lQhT8DXZkeOj9iJ8ovQ9Ht1K2sjLyL0KjseIpn8z8nGouJzw66PejqdD9Z+tkPxJSP8H/o/wAb9fks/qyLK7kOPqxH5Ekdiy81lax4WyHGo4cjlnbFiKF/JKYmc3wXrxRPBZ2JSH7xYnRKdlWJE0dDodSvgirEqGIbY3mij0KiE0N29up+s/WdHhRshxVq460Tj1OO+xPx43ssvwS43EhGst5lqmctNHH48i1tHjT9likWSLEzsN4WUSH4IaUVrETEx5el6Sjp94eqeLHhfDLRbJFkXh61s8fXwWfYvAmPCLLz2LLOPycnvVaqiJ3IPFZWPovCEPF6LeDL07CPoYsIkvOqy9V7F6JrwdzuWQPofsvEWcjoT09YSFms8fIqOSenFIiS4bGqZZGQ12QrE7wnlYeaK1rHHyD5PBLydRxIcnX2PqxKh4WFW/UrRFa1uss//8QAJxEAAgEDAwQDAAMBAAAAAAAAAAECAxAREiAhBBMwMSIyQRQVUWH/2gAIAQIBAT8BsxeD9s9ishb2K7PwY96uvAyOx+GN4+Bi2PfKaiQrRk8EbrdqNVkzN5DtKWBTySmkS6lfhPVI6aljl2VluwJbpD9H8p59FDNT7EoaWV82pRyRVkfovLNj9EYLURkoIq9RqHkUCE8SIvNsiFuUzUZW3BKPA3ycs0ip6idF04jXJ0r4wZshWyajKumajWd07yJ9dGJ/Yf8ABdT3ODShaHEqJFOekq1O4jSdN9jQaReHJklXUSc3IwKBQhpQ0YJkkymmSOk+/lqTwe7JEIi9Was4Homzp5/IVU7opmVuzZyJckRrJCJFGTJlDkL5eiWUypFlFfK6tya2jundQpqzlhEqufWxIUrZtI5RTnr9lfGkoL934tgjUTKj1EUJCTtkj7vmzKT0yOpRTXi7WGOBggYGhLc0L2VHkgZMmbJ2zsaMEbYEYGOytg9i2q+bY8DMDV2QXgyZtgfHgk8Gq83gh63Y26cD5GK+DAiRpNJpKqKT+I9y2TNLJrAmZsrMz8jSMyVCls5M2wJ7asTGzSSP0RK00UvezOxbZD9kOWds0GkqGeSPocTBIh9t+bL1ZSM2q0nngo0mnyYvVhwT4IdRKLIvKMEqZP4s7ojA74PzZkU76jVerR/w7TKWYxNQplWkqnodCSIIQ/FqMmdmo97MjlmyY3bnb//EADsQAAEDAQYEBAUCBQIHAAAAAAEAAhEhAxASMUFRICJhcTAygZEEEyNCUjOhQHKSscEU0QUkYoKi4fH/2gAIAQEABj8C4gOM3N8WeEDiDRqYXxLhkHYB6UvAXanGOEcZ/gD4RtXZWbS/2WM5uMm+dq+KPBJ6eILjeUTxfFP1eBZD1uJued6eIEPBd4g4SeP4ax/N5tDwNHr4g7+ALnHWfECA4RxfL0sbNrf83wo28RvfwB48cA4mjqra2/N5N4U+BTPgHgC4eKeA8VvbfhZmO+XA93p4o8D0ub28UrE/lajhzTHj7m1CPFgn9W0A9BwNG9fAm1+HeP3VQfGHiQ3NS7mf/ZZrAFAyaI47Cx/FmL34I28CHKrAq2YRDMrsUSudi/FctouVwK8txRQ42kuaAUTYEyNDrdgs8bj2X1XizH7qRaOcj8vyjQLzL6bZ/sFGL6js0eIDdWxGQdhHpeEfAqHKjlQhO4qErzKUUU3vwYmscR0CjCZRtbY4ABMKlpAGSDLbPdc7Is31Duqbg1VFNnPULmX+otRTRipDR0C6cZefsBd7KTmam9x/hTcLxOSbhyhQ5PxPpCMZIVgIHKyB8zteqH+lYMJ+7dDG0AALA04SvqVXRczi3qEaz1Q4rXd8M4B1/gMrs+H0v2VkWv0qQg0+XdR8McUmsFTa2tjZD/qcvv8AinDTytTba1n5Yya0UCFm2h6ZIDUI0uoITjigDTe4cVhZby88Ebfw5PTgIJIUfdHuqhNHxDPo2lJXy3txOs//ACYVbWedmyoK+Y7M1ui/5bjGxUWg7G4Ms7MvcaofNNm7drCMQUXuH4AN/i5bC5mD0VQ4KA9vqqNAUOkdqhfMcZI1TrIwHjJNY79SzESU+zJ8xgqAcmp07qS4KjwvOqPqnA1c2ouGcOIL8FHHsUGD5TLM5Na3m/7r65J9p+TibyR4dKLyz2VRdn4jGEUJqiGwGigWI5I2OGDuE+WrH92RRb6hOnJFllpmQvquMTlKtLIiQGiUThAUtyTrFzyMbcoRm0d/SoBc4dQqCL7Z2uGB68H0w2u4X1vhLJ/ovq/A4P5Vy/E21l3qv+X/AOI2Tv5guT5Vr/K5c/w1p7LmBHe+nBzMYuVmHsVyvd6hSC0qtmVzMIVL8lRhXlK8pRtOilyPy7P1KBBz0X1AD2QOjk2qcMlasINVGcIvd536LFaaaLHIC+YU6uvCxn5vn0Hg8tq8eqpbk91FtZWVp3C+t8AO7VR1rYrK+iqqLlqd1usgqtK8g9lRSaQh9Bs7wuVgCqxp9F+k32XyrNsQpWEoDIjLYrdx2WF2hUeqk7I4BWarkFVJWCxZVTaHE/ZY4zT8Nq4TWAvMD3C57Jp7FczXtX6oHdM+W4ODWQsgqi7NUPi14KXZX6LlVU6IRc7VdFymqwu5h1VGwUTNEx2qlfMsqVVYndVPZFrAZWN6AWIYstBKrj/oVB7rdVPHQ3Vatlnfkq38vus1HBmow1U6qoukrSeiw739FQrmQITZMEI2YeC5YweVUoNzqsVF+Lf5kAAOpxKuSdymio93uvOVVx8bO8F5gKVVUyVFVUX+ypmqrJClFmfdZn3lUqfbg27rz/0hCpC8zTRYmyR0WMvdyqAQAsRcfUryktb6qG2UDdqb9Q1Fw+WGupUEKjHg/i4Ko/gaBblfkUSb+pUkoYGH2WFeYKsqkqoVGhTSUVX9lyhT+5yCrzHc/wCymYGqzg9QvMnYGUdVYrTlHVfLsaDe6RU/vf1VQq2YJVWwei5S6EYfkuUYlzWbvZZeBlfr7XUcjSVBkFeaimKKS0KhXl9lzYj6qjSPVUcF+pHqoa7EbqKiqsLf/i/ypFNgtVyvK0UWjzCq1GayoUO11UlDsq14K5KLuYA9wv0h6LlxBSx89wsgfVVs3eyqOH7o3ULC1o7qGFZyUG7rIqSVyrUlZVXX3WypVYjE7X1uABWVFkohVUsdVfUsabhQ19bgycLpof8ACwuzbdS/CbwRxQqLQjquaxb6KmIdiuS09CFoeyzGFeQGFLQYQrTrdiQJBUnLtfkVhC3PVTqoaPVC+b+qqhtdQI23w8se2tECWu8rRUe6NWubudOybae6w7o9kbqqjroRpxZrdcshQpWS5qnTCuZzYVB7LCxqlzpOyEM9l0UCQqmTsphTmVWIUNFVUySoGfDS6qohCwuQEo4c1aPf5iGvw/snm0gWcUM5psrGUTWpuyWS3VKX0XlN0aqCo10ukLKnDgyUAVVG5qn91CMLEf7o4WhYrQjssKqKlCM1jLqoEcFb40uGFSsBdosZJ5hyg5HcLAx7t8GqBFARcXRqslS/K6NVW7JRhWyosQ9b6KEfm24YeymWFn5AyqaoODP6V5XhZo3YayuiEiUbWixEe6qZUarp4FFWhUOQOaLNQJB2Tm/Mfi8shWOfkGfZOLU6KXdUNCv8351uyVOGl/VTooUmCFTEBcWlykG6AKqSskGtEqEeaEaVXXwJQUQhhVq/ZhhWlrZlzPm4TA6qyOfKE+6l5WayRCMcHVGLq8BklgXRf+1LalCWtC0VeASVmplGLp46KMihcHK0szqFh1aWg+5VnP4hGUCLul5QQPFW7JYSKqiNVjsqEZ9V1uGJvsqNlf4WQVeDKBdPHldTNUoVDoVaiU6R1UH7lbWXqPdWVQeQVCLJ9OLrKCcOGgu3u6rlyKwzRFo73ZLMLOqwzTZUHiUVbqIRKhynRYEd0Hbo2pAMtwqdgsYuHa4z5jeUHqQpCjIqh4aroqoo30Wfi0KGJaIQFCE63B4zCBQUnJYW5I0MIH3uDQiij0KjdFpVMrpKngpfhN06cORVeOnD0Uhc2a6QmxeIQlURkLM3YeqLusXSBFEW73HhpfVZrrcT48Kl0uVFRZQqoIKFJUIM2UqqOyMZ3uGymUHjJArmoQpDm+9030v1BUFUupVUzVVW6FnxUVboGakoKeCFK5UECIyuqENlCAGyKd2QRGhqohZZ3wuou6Xd7qKSobQcFeCvFVQ0Kq6XU4aIyVA0QfcK1uBRWI5aIrK7uoOnBKnTgrcWjIIKIUC4RfXj5jRQxt1VDQgb6rmyu7qiE75oobKu9Lh1Kw7IlEdbpU73BQUUVXVTfB8OvBV6kuv5VjKDOq5bqp27a3ZrlzTx0TQMtVC3CO1xKceiG83RcJyUaaIOC6KdCs1346oRl4EG6uS8yz4C7YTd1uKLbmojoqL0uld7jOSb1TW/amroaLoo1Rkcu6KImoyui/bhEZoeFhKpcE5PO5jg5qSsQzFw73PHWVOqg53Q6/tdANL5WZqq5Iu1R2Q6IHwMKy8HNdVkhKeTsmxrVG41gBZQsDtREotKFzzs5ZUVFCrmqkQoqjOoWazFVLSA5YTWFXJBDtd2uPgDbgkXxPACFVSVa/y0CgaKqosGmt4egmrEMnLCUQg4qWlVUO1VJKrUdU3DImhX089t1zisZhDrcOlEQgVF3dV429lRQnO48FwqoKtGRrfWqwjNURbrcEW65hQc9QnN9lXO4jqsTc801/VQNdEULsBuJ0vx7UN0+BB+0KESjYjzO4wUHC4TkmOx4C3UBC0a7HZfltfKpVSaIPaRXZBsS03fMlzXdNUXWfOP3XW4yFIWFY9Qu6BUZIQ0zKojOgvwnIhEItN1VTLhODVB0hFrZNNEbR3gYTdJyWFFlpDmOoQVaWI8uY4m7FCL/nN8js+9w7XBAShCIO6wNPMFUVzXdFRspUlYt9VpdRVyWJza/aqKiqI8TEEIQ2Q2OSCZ8QW1HKVRcpR5DeGlY7Q1yXmQcMinwcqqfVMKhRrcZKMKQUMUBw1U6dFANEDveWb3G7Cugyv6qOGvHKoa7J1naaCWnqvmF4HRCaNLsSw7ojZGVBaqUWKzcD0WF4K/VjujZveHE5QsInCd7gdjfM3A3Gq6HRZXC6UHDVdbhObrgLqoniPDULDkuVy57Z3oVlPdBURUxN4lFtpZAhBzcYnqgFyiEDoiB3UryZKjYlUCCOI0AXmzRhQ5wyWXA5iBCk+Vuak3deDqqBZLLwLR+zbqXBC8IKmVwGyF4YdFLdUcTf3UGhX7Jqd1uzo6ovGULqsMIFCNQv/EACcQAAMAAgIDAAICAgMBAAAAAAABESExQVEQYXGBkaGxIMHR4fDx/9oACAEBAAE/IR0gplC6vnhsMl4HvxF48GLx9iEPY/CF4V5WwRPOCQgKyvgdhnTcSyr2b+BH+psEApi/jainAh7AM1XHgq8vw9QqMFKnjto1xaLxBiNvGDp34TbWPC4MMf4NZ4Meznwr8JVl8KhZGl0UZ9f4VhlX9FGccj8w8/B7jVwUUH4J8Tzgx48pQ8VrNE4M+EbHIsnwZF8xyG83w4vC4KaeL+HMEqPY36CjPFiXVYSLm4YDQQ5Cf7hZGwZkWEkMxT35v+BDAC0ULg9lD8+Hvx08M4Qx0ZHF4dV40Ya7/wAYEjJi8E0dAgCG5ovGJUck7f8ARMIwQXRfRHZhlOTjyxukCdFQrZU5RohPRnyhya3hFkBRmdPBzyCPBE5mhEi8RgOAaKT2aFNC8FSm8H/ZS7f2UL6Ej2HWDhPDJgyZh9IuxexZvJ1PAv8AhXgap4SL9EJkg6eO3kXxuOoNeYyQkZIhCj0SEbUQXhLLlf0Oq2J8uBqiNBE3PSyUOxz/AJPyTYO3xLRsjeL87Gj6XaeFn+D6D+CKUeDuLHYwGRwgaioZByefMH0dr6YDwLoXL0LX48QPX+C8peaaBBe3kmrf4PXhowawxBXh08KvDTxjw6aC5PEHj+2+ReJ9PJwGwKMpzX/Fj+Y/kAxCeKrBn/BHJSEOtjHh9IJBETehidQ9j8qHAcY6Il8jFOBqJsYi+E/HALih7VfoM7eYzMi28AzwNvLULuH3g31hsQXBkyITSQfjHnjxfSaFC8Z1b4aZ5yfwjMrU5yo/7CNgyHl8PRH4MGYZJ9kTsTp/hMZq/vJEL7/pEV5F4vIoyXJ+RFT/AKGI1A9vCEmv2ELojcdRsC5v+B2C0Ef1aWHi7CH6MiGPODPjHjAt/Itf0eInvgx4yZNMvycxf0Yxtsije9kgF5vZmg/jVCxrewWE57BCVToatl+mugxVo8r0VYojMzVBoG2YOXZ8DfZonDDTupp+A5qOa+Ghf9IH0QPJ4MPwRjXnJ+Dnws5HyXG/EcVyUZRXKI6FDHfkYkIsNCkJiWsoQOM4PUFjoZqnW3ob2DA3mbLP6VAAk2uTkNLPDB1AGhhS1B00mApcN44D/QXiGseTp4o7oPzvzI0OWr8XxPYt+UUGeCQa2IrsXoL0IhXdLIPwt4LS7+nsfyGrnpxCrvEddZJo/BFv9IZGkguH/wBRcmlN8SjiZeDL7MrRkukmkITCL8zHgUHqIQ2EjJL/ANQiIUeHoiOg5/xnjg+h/g2zQ34V6J/hfYhgz2hEEjEsTwKSwuXnsw1ONOZfA8cLMGPH4ifAtyU3v5EfgigRsjsLB2ub6D/Q6eCbracD0yeRA5zbvhkXw5vBCCkFDxnxgW/MMU0ZKMwaPSZpS+MGDHhPFb9pG3+cGXPebN0D4SFc19cikn7ggcDQLDu2hkWrl6BuyKkEGSG+UEnf5LZlemLdfwykoIQGRp4UkJLqqv4GMGSOdeeffwotCGUPRljHDyCwqwfWNxcGsM9mfOTnytssflE1ZHLKI7S9o4S8T3rI14hnryx3/ik/RlgwCEbYJ6Gsj+RmJIEMzL2Y/wBAQk5DZp9DRmgM+bckWBqE2xDAwp0fTMFZYZ9bMFgnJqf94BgcE4FnwbV3WVjyJ+SzrG9oc/eoGRQdQMWDwCfyzFfHQxwexFylfbNh5J4cJfv6KZ+kbA9hWMfLAtMwP4eRt/Akhsj1C7AlrK+DqP8ASQ/4B8E1ovBBFFEgS1TzUH1XBRX1E+tG4VSmAWdEWOqcm4f+hbagkugloyNwN9l8D0LZhDkMGgIMeF8ZGej8OnAohKVHiN/A21fRNgGz3o9oynkJ/sGWgZ219ssMnmX55TTeHXa/DMHdQiqog/h2LBSGYRhxsqGO/Yy+xEla270fRzq0eQm7qDcx4UDIjXAyxphThg3YyLS7P0hF5mFrWYVGiGeIatj8ID8/vDlr6QWmaje8lsPxam/EG/RqYGek+SOSCrvzcFcCJZJ3CLOTCb/g4qWOj9DMlhgEXsdh1Em4QiVH/I1bqdPZPobn/ASKFY2HJnTbHItjJHgdFy+oN+DADI6vZ6YLbzXkkJcfqEWzGybuj2xE0f4Jsd7ifa/sDRu+sMwUYC/ARMIroj68ZKyokK50mbgXioTNfzHLHiRGDI22JVd/6NlfQhqjJaUYZ3cHEdpMX+hgLn2M+weFf7NinoYRCvPg0jROQwdiGBfGjuFrFTkn3iwVZY8AdKSurg0JelF/TMkvk/7FeEQ6aplCxk19ljXz9k9hg2Y78Y6IiWX2UVt+PyfkSuQ9rjNfRCEvRS4RlA3w2qHphOCo3ESDE9ra/WJWpUUDavRn1D2Fh/sDIbMH6U2M7WxXpE2rv8gjQyIFRRz+hhD5EunUgyunvAhcn+BGJT9wv6gsy2iswwyeNR/9M18o/oPkejIT0xt34b4K78fgRQz8nrxHRJ9jYilvbLsFo0yernpDaqtGH02MtaH3IlhftiBKPkQnB8Fs0/SjcldMZZaez+5UytmDg22Jg+eg5xE005zBiPe0f+ez4xBgGQiTj8Dxzwzp3sQQ+RnsQjjmmXBPLHHoY5M9ZXtoRazH7cpjkO+BPIzemXsZb901DK1uCdrxwCZcH5K1f4E3R0o93hNjqMGH/BJYjbjCBSdGGB0oEjjFkguqbRfkMYdSCYqXYeG4/pBNPgIAjbj/ALI+3IsfZjZ0da/87EJLrf8AwGNp0In5siPExBlW9tEfyCG4Uc2JBZ7cFHFvQlLzogxcoqL1F1gGnU0O0ZEqyZ1LyQi8h9BLDnCr/AxjfmpmfCHR/OP6DUdI+ojgbrCY0cCeh8v2DYLRsn0RDZ/BP8uNHsaqfgRwDsY5Rnllf8t6G9SwjSf5BySUf3g11DsLk/iI+jIf/Qu7emPgs8iSkGmvAy3HoYVk4emWTsywk9eTTORQNDLDGEc08BnDMpGTRtRswdG9acDWCmx9MUZh7DujEenlCvp7EmEfohdXrBLfpQ0ho3t6F2xJ6o4j9uRV+m7GGR32Wi92BkSfoq1vGhSRezk38KG1Nz+BsmcvsaS3+4NkNLl7IinZBGsn68dUw0YA9for2Do02M7suxNGOKHlTYomO2XxxBohjiTeKKSC32AiFmfsLe2QhoqUgQDz7FeWNrt2JxsCS+wGIYGH4G8hOCq+jQMujMbxfDIQ0+JbW0/emYNP1B3/AGGahGR+2iIsKgbQXu4HxrnC3/IOkHYo9DgM4IpwElyx5nt6F5v44YwPsa2XqaMguwmEFwzYyFBfKEYER5GmGYOkF6VgSsjEEyJgyFLqFThLITUzHbaGKndH8YtGhZA17GW0KifgKkYclMiVV6MkDbs/oM5Seij4BugEgj3iGWDKy6Y1v9jLlkW1fgYdGcwj+JJjvKQT2Bp5SIhTLPeIlIZ65OQHSEE2She66E5YQxtP4Eoj/BDc2xp4TgLqH/I6oK83ZlG2NMwQyWG2IHwAAI1VdnDOOuWMcBGlRN+kfA2/A89yv5GpXVMbA2OhDm7gwy5I+9jyDFS005huGdGZIrL9mVxV1RUqP4fUuOKDCHXvhJWfzCNn7ES/qVFbx9DTJgayNvs478Bs6Ckqj3gtYkn5GFNzNOgEXoVLz/oZhYhBkErNzshZejJcF6rPJkmVEDLsFy3kStywxv2k52heUrn/AKuRqNVnnIQFWloU9Jspu2I3GhuSCD10HIddo1zRrJh8CuV6Y29nln7TRA/BHps2IZLodEyGKIkT/JHU1p0aoqYnABCp8wjDMFv5ATefwO2MmDjN1itpe2aCTkiK/wDs/hPJ2DCrl+xM2k9jdihJENoiyDleDgMEOcifqEm4/GP2h6xeC1d/Bl95Mbfw/QCMdFNkGpoaTwLkcmDKRzDKFGKIB+/AjtXKEXJlwZQ/YhCLcRVoT8mTQu/O0xBj9DGN4Kngh7G8E7EpFP3BhIHSqlOF+zLsVDB22aSSoY022MA29iS/Bf8AQLiUZ1sQPwORCNv9EPY3ItQqIyQV0otJZ1R3/BIQIz/yQk0t9l0GKNlvIRZCqrBsUnNNNPQlgK2TQ3aLEaZ6iaDuMVmi56cZwMJ/U9mFHAMSKiWhHKh9yYpcubDDZKRm17Ju0Ygk7QQbgbC4oxVy8Ccv9iJqkNSHJRmQsk0OxcL+jECJmRYyd8dDaCxadBloLIVaOMXDFhSx8E8CTnkSP8IgeRhu0YC9ZIxTa20OdTTLWxJPIVt1mfn4MeDcFB/wGInwOSaBiyjwJdMI04PRafwDZochwQO3TyQiIcjHqGMJCq4FaZWOEKxhFXIdjYpwP0BCEDQvA0hFBc5Wdi5CIU2+6EkjWnvexaxLgIDLkTJ8jhVoFNC/oHz9IlzticjNGWNGewnk0fkq38xp1OeyQ5Cvh2MSVRxUC9tjU4lRDQ1GXrj6RdC6JsQ22E78BpVFlCdjXSPdVIh2UE6UHNmJoePAZBDLT8RDyKKEfga6LlBaO4KQK8v8A3Tx4EfoPSUpNoXZAqDWkVJeWMxGv8NmZD+BFcwjOhwn7F8wgkYjDRCZDV0SUODURKzkscFPYnvBElTKGZUZ3shqNjhVobayR7ppo6I0P2Naj0ZbGA4EcnoUlYN0wZxRuTwU0ZIyFDOmSsNCatImYQRE66b0KgUzrA8M4LTSMRbKOJ9k6RFzyJSVESRrhmQv0bGiR05Dnr6Ts/kT/Z6BRohg4g3Wk2PQUJEZQYi5KZIngVhrwdlNDCgieDY7PSRCRDEwGKQ5DCaRTTsdFlSbwLjIaqMivgrBNJhHpEOk2xYA1hhGVoPZ3kuWnLexWPgR6yfpmeQMtw9DGABbKiFHpRp7MSYPIqWUgInLPyMk5p2NwJlkISoOJkiSRDaJncHJJMM0E9nJ2e7AyAflyEywx6GqGW5EeE2oZbBK4EjozeCcGH1spkmexAfDFRJGCaMnSJ1RswswdaFt3wEM/gGRtXAqE5G7vYjI9mEvoZ6KVp+DsRg0YDgAP7/cZa07i3iwTC2QzJLA3tfGSj4ePIYTxMfwXYGUFVOTEFQmJl46CJDYsieYdzIib6hImbk1EvskEVG/aGSTBnElwYJlUVti4EU8NOxr7Wcml+Q2wTjT2Pi2xUbpw8Ctw0NU3C+iPAxhHBOxwNjW7CNFMZu9iyXFYXoCHStENMg3FodKhyBUGdhqMpSyERmjZPiMOANzTMIvI8+ZBjDLFWEslYL2GEbLRlcZA/AwK84J4X9BKg6ajC6pjYLA2uRCw9gxdCs7Eoxh7IQWB00YCS+zI1JCZsnsTW6HWtBgFbOnJsB09EpXThkTsgj8BkRsiXROgZW2M9oych+CjzAIzUaYLOw94aRsUkXbtExgYh1INI1DQ3DIUfTGsXcVpg2VsZZfgIhdv0N/UIeIRZiQhzCOwYx/pgvWBoMnzImmQZ3EvhCo2xh8ATiizQSYcmbR1gXhGVyYL+iJFSzQIomAsMth6xJXD8OILokFhirM6QmYIxS3ew0qE7qKjghBrg/gQRh/sSx/S59Ao652KSt55IaOdna0ND0ha4pbFJqZDRr/AA7OQTXD7Ia8FCvaI3GBlbXfAbRE1sCzUEzsmI2LGDPEOdLxWzM2YItVMw9irDSQlIi8Je/CMDvHxXAIzIh7bzB2N4DU5IVEQj0BuJ2i25GBdl0JUYaHgSPEmToNTo9Ie5TSFGSwmZ/TCJ5gwOB+FESoRhmRFJRUaRMhEvdqh112MNaaTVIf1GhjPR/I4z4Yg2iJhIXJI5i6CORHYjZLwL3BgLBYEZoOpVOTH1xcfByROQGIUaYjBkWrFZA7kcTc9htOZ7QxiaJoaPSInJZ+xMxMGTvVij9TEGr6AKC8LMv6xpHEyF0oykv+glnqlIcMdEiNKuPE9k8IVOhkqIbyJhqnIlFGQZiTOkO0G9owAWosIcgaqOgoscQy6R1Z5Gc7GTysj9fojyHosD1ez+iZLHDEzwshVDbMwLEa5JKyGRDPsHsXGHqiMDglL/YIbuUuAyMsrRmnwasseQzW8bEeD8+KclIqcwG1H+5nwyQaacHb65FXGSPJ1MVNGDITzYw/A11yOSMBDgpzIOgy3QolKLYOysRkzTkzJ9HgoZ8GJdTFvX3fZF9R/AySbGEwCRFSmUUGoYZJPQsI3gZCBbfJRXg426Ir6iniFDdPmFIPLQO0OGz6dMm555r0ZYi6MhZiJMDRtIS9Ur9CPx9EeOdHXBSOxmS0ZcbtgW4djpqL0LGEr34yKiMb1vyIwZarx+x/pQIgZPbxBTnKhOZNPhofRAbvQ7EKFNeCyV1mMRoDyzXownfslWMUGTR4PlDKMQK/y9CXCMAyNlG9woA+iBgaWn4DS0ZIzO/VmMl8qwUj6Tk/ACihH145PyNclZs2isTkyRFFOHowaQRWjn+HxSCMcHwCcb5DtFqmhi4EKRlx6FN1BM3Y3Y0IbtHYAc6D0DA+QhzYhDGRwv0OVblSmgQQh1RjSz6LSznBhA0b3RBZREQjJWDeylY/5DeR+LthR4RaI1oT2cwj8djgaHIwQS+2eRNW62GhFNylE+WeBerd/wBDHEyrGxCj/HkX2mVTgN0z2AxlIaQ1rFDTAYHFitGBGBvJ600RqaPpBCgw9iNmQslI8+cp7qttSsoFj0huAh7VPQRSXzR0j2bGKTH+ilNdSnsp5SEWVDE60QTNlkdGkkKdD6T1CeBu6QaIhroSDP4pyIKHIewjawligEoy4aQiJ7KZmUb7Wxi38Rll/aPdfIGGHIJtcoYxH8hWh0Oohsh+abMwT6g1C4GG5Is0yumR3TOLlC9siL/y0/QCNYGLe1nSE+WZUMvQnIwz+i0yfDHHBjwTkRU8jXoimBh1tQiJ70ZIY5sFbE6F3Ezd5ERJhCodD2TkZ0bkZdmAI6gZK+V6ECCUqmBFPPKEhIhcDdo2TcmoNSTV6OUBgGBkcHoZMsEFKmkBnohrM/yDUVTk+x3MmyANGCrOM2H1FzYhQ7gSQiA33VbYx45EtH7KfWTOcvZh6GQOJNxH0K1Yq+PQOjKaUH/8FS5sIhMylyfAigfs6Fb3kSSpKD3ExjnjrBhmJKpiPYZQzypzhGieOBsQW3b0HpoyJM8BzV3BnXYOjgffRQsvBvouhE9FR+wNCiaooH//2gAMAwEAAgADAAAAEHEV9wEWmhifauABvvy4c8Y65fYJKWqkRoHm4CNiKGtRWxHghZ+yCaIGAYNri9xKHWxJIwcs6oZcQbAPIwYQqZ1j1FPxZVYTEYyVZcCiCoALbbh2YivpFU11Xz0YSZU/GDk3z4B69C7YKl58y7yeTcad1IZURR6yGyDiD3xGMxeP6ZYWXwpc3UY1NJ1RVZRcAOt8MrgnQwSZNM8YyfogTogrLmRx634PkyIgsBT6VoDN7Fo+b1aY9USowU6sixA+iPAmRRIO9CyGOCDICgG4kAF4qFjxU2TCgy//ANIZsCmIiuFkRoNL3uZU6FdmurZaopUqIx8TWRc4dWFMhN4meRYchAqPv7dbSk8GuWo8oT5ghyYPQpLYm/p1qIFFIuJYkHMj+pQIFCCyAWNSgDuEAsZPMqIZCYSdw74SipimIBLk4XnFOH0OEHAc0KHCEjrVYAThGeGgfCEHhfBopG6mx1I6FC04hARGLwZ4qMxAhCdakKNR0DveAJtAGI5IODeWoQO2KlVHICAElQR04CHFRAU/fM4NdnJUAyHD3ZrS9N6rQK0JwMIbIGMJlQ9VMIv2sbnvIEoAbdetI+9m1EoN836TWr50y0RJrdtZxYGHswiAenkCEEBn/8QAHhEBAQEAAwEBAQEBAAAAAAAAAQARECExIEFhUTD/2gAIAQMBAT8Qh4M8HI9QZ8fvI4ft7vEsvwF5+HyORyvy9R2PgeRG82Oxx54JOP8AlHwPI94HAPPqps13Y4fphzjN5EexE3SLY3XhJQlhCvy+Hj6Js3nOdR74mAQmB399Z/boiJfvL/w7871HqEub25O85ufl+c1W8TzjPtqWfWyZxA6TF/MID+yp28uhQrq7PgG2Sc9WWw2WRaeR2vVqH3NtLTdC69I6RIsWbN7ByL++Qv4XbsX5bZXV8C7LIc9s3P2Zv19EuRSyzq8tHWH4Q1nkbl7SLb9r/K9x47lnBOcs535ZrvNPnYyNznuWNksjLxst1YQGNWiZ6Jl1N2Zlz2W3bq2CCIJGX5J0hY+E4HLVrieyIW9S21thLIs4OMVfaJdX43kbzg9c1TxHhny9iWHIOd8kzrxnBKU5Kw8yH4O/MfSG3dDHKO5ky/bcIds5Xdvwbds4zjYPxLZ7OB5ZLnAb7d3hhFuQ/wCTwT/m3Z02vHVeULbD1Mdze2AdeMc48v6jPyTr4l3thLZkky5PNc49jvt18ta7zGeQ7JjxvA2bHWU4QDboz2YuO4z4AbZPXAbcjuPAbz0h6We7ct64vTbIkhd4dZtpyBE3WY4JZOeegYXonnByQxjbqLdg9x6zPAW7p7slx38tkmPXqOMs4dj1B4wHSw4jfk3Sewj83vhczZtmQ8BManGcUcFnGGAtyRe4OrLy9fD/xAAfEQEBAQEBAQEBAQEBAQAAAAABABEhEDFBIFFhMHH/2gAIAQIBAT8Q8+P4sM8l7DMPD8n1++rHm+vwGe0iy7jzZ7PJ+x3z75JPElz03x6/b5n3PCXX0+jlv9by+Z8fs+S8/h++dJbJv/JHGp6SHkdj74+PAOsXRD6t8f1bdZDR8/hfkfwXv4m2QZZ7HgiBZ1T5BdG63wtiBPzwf2p/WXTPAXVwN8RFs27GWx9nr787/P8AtGvLfdksA2z1J3nX2ZmSA/3xfennIvnzrvkHkI+YWoZCsjtyztmPyJF1jyfY3yHeyyYbvNqV/kMhS20jJCf+Xy2eoKXKm9+SXw6sNz2OnLXL+wAh9/x8tLLLGRntjY2HCzUlp5HI9udn5Fc4v9J+i/0gMbbXJNsukSWyyLbuOx9kH7f4+OfIiLBwpYuxnjIWNp8x/uP38Z2LtDzDsGx8nb8rfK3UK8kOUG6uvT7b4l8X3wXbssW/xnt0hNt3488MWfr8kwIQ5fkb7j+Rskn+WNrv5cwg3bzAJns3We+Fy3B/J4zHlcmNsQyJ1c+Tclmwzs9k3+Y89zwk/PSzg8TsX5MMO+HdnPPD+Rlm3ySDnmkrczFjUdSdg7ZybYcbZHOnbNs8/wC/rDJFLJLLjrPcc8ph47+W4QVicxDDW2G+s/Y8dJ9k8YaX/Of68C5scJJZdA9Nny6+y/CW7Onq/bm25J4uwWhLg/LLYUOTw+RZlr4flsO+FD7ZdLXgX2OQ0l1PnAIJACGbP2iOy2n8RnkJvyVvscnU+WDyJPP5dKazwSeW2oQkPyDcs2hybLhAlpsbNjFtz4+XyORm254trwpcTJ/sWcsQbiD9jt+p2UMb55Gztl/9m2+/wTvwTLkKX1tw8k4vy/O2iybsrDsN/8QAJxABAAICAgICAgMBAQEBAAAAAQARITFBUWFxgaEQkbHB0eHx8CD/2gAIAQEAAT8QeEl6vuwgHKNG6jlX4dKsG5ogXa3NsOKYzL4wujrP1HbbbOolvxwCEVZhuGpzHXl+DR3hV/g/Kly+pYmBLsYdRUyrmMx34z9Yr/A6qoFtRCvLL1hsuj/yGMB5amd61KF2wlxcAHxFqWfjcWMQQR2/JCWTglAxHFIh+IOcDTHWY7MCgivu25tl4WjYZfxGhGAQcRwx4xiSy4GovGaEoknZTMFzXePFLOs1LM1O5jzBmHMrNOqeFf8AIm2Hbtav8zD+cNH5Q2irauXPtbixM0N/jyg2xG784nrY/EDd1Kn2SxwI4ky/DrczPv8AB+0/t/FlUlfvLfNBaTEQ6mE5VmYmPBKrixmbPlPJ4lVLXHMunyy/wRjdRm2WxqtsxUkyh1viG1xLdhQnf9clKqG+7qPxkrblBfuOSzHJExDAJn8GlQLphVM3Mmzd3H8gn3EvSKpBj8A9y7gZhlDRGxFnHsIc5gs9Q1LSM2AjoRqjtlIrAdynZ6pmJe4UWUBDwXLfk4mVXUsKI+Uujmdlo3sP86ypxi8m2NSMjU3Z31HWId4Zki4qhkYCZMXGNbaiichLHaEdlN/wXKxDy6hgR1xcfxB7lkIWB4nZCaZUMX6jBFhAs6iddR58R/ir0YEzJuN7HiJW9zRzZgeXMuVbmZg1EwjpmYkLdNwAOAp5n8su2OZXV8IpnMJcaxPxFfuOkP2g2/BuCjEEJftOKTKHWJmTOETWXYsSLRiKzEyB5grzP6/FiNrfwtvCqgh0Yi5zBLWxsy8RsuepD+oirfMMFyFR3jJ6kCDPpHcPEWBbef1Vt+iKLJd9f1CeLW5i7nKWr4JfnNfx5/CvcXMQYGSDNSnPiNXY6P4rUu4rnKzNINRbmTn0P8yrNZYmJ8VuBZDUxDz+Cpjyscd/wVcTNPw95WqHwYILRniwVHa8x1DNhiLcsC108P8AKwqvGo7TjXB2FtD8dZv8nJNkqXbb4uUocQ5zMQqxFV3TAg0S5z+BVBfYY78UKlPEogZCCq5R6hRFmKpHG4tINEYOJkY3HxcvN3mE0lTz+sua178G4ltFZMX81POaG1yMNS4OJlYj3gP2K/uo135ltPc1uUfyrMf/AMHmKQZ3GbVRgD6Y5Hb4pFZOpiQ1PkmJxmL1KatDmVEx+J4dLZg+gQL5gnWiQsYMdocISPMeJpLiMVTMuTZjgVGKl+rC9n/0xGIh4YnyXdcHcrr8R42yhdsFmOCfgSdch1L+l/rH+glF0IHFEsJ21GNUzHjH4MPxVZhW0qLw7xVyvZTIgxCh3Zr+J4gmEHZFRLtRxC/FM5T6E/5C7VXSY5qHlqPVrOXcqrRTMk7HDsXi4fKmFVfwg6ixiDiOFNVizWOMrT3ju/DEjWK9ZPiFIbglavVR1MC7pV6g1ZeMBD1HJk2U157iO1xy/TFLbFR+RlTxQV5+PEfenmc3cuPC5oVOX4qjRB7aidWHwH/lmZCaWli6/jncVl9zc8IH4GHmVED5kqXJ6rmsC5F+Z84lWkKaZecfhk8RG0fDIdQHwuUdX20QWn1Myan1Chom8zSIAvmJMfK4L7/UYqFEt0XGoVcOsyx8ceT7mhB5d/x1mWawN4r2zLs3sxYwcvOHBO5Cm5lXS7jv/wDIN9LkfWpv8oPhYhxzGUhmqvw5SlK//tPuLU11O1y/jhRgsHNUm+J74FfgeEpggl6N/M4REZE57YZapFGocVQq3zJLb1AWpTFQV5Yhpfc8bWxtbepXc00Xjs5lSDKTFFQM3LnL3bFodb7cW4rZtu9XE+pXc0RoUEmF5ctB9sKKhdCJ46mWhCPOY0UmS3FlnENq4xCe94xmBwOVpeua4lcIC7bHySopXQajb8Y4lBoZ/vf1JiNa1LKr3HZHN1ZlzNaqGWGH4a0XHMOI8ucs1huJd+Mx5mOtPMy5f6j2j5g94k6B6Mp2pNa4l83M50pXmM90ejcFFj6xj/sKT0csfVbj9HcTJ7JVvRNm/vDOxFqfvZ/Ld4V5MtEg8QxRwSgUynBp8QcBon94VUF3dQEUGKi7LbYy5Om2BxFs6ioeJm/KEH4agqUqDcYjaN4P+8ybbBKtOTKCaEhAfi5V/gFfhy/pGFrKE3PJNsxPH4ly7lVOckGCNIgsKOK/GJUOqASrcx+U0dzHmFIXrWNTNHerq3/3z7i++M64jjUbBW+R7GHDcj4dRrSkLIcG3nqviBunYurqop0UsamWDNRqUoiKJMwTE5nMe4C2O57iyHicXY6h6S9zMhZkExYOCa6cDMsJW5xiO+Qt+2OqdRAuXDozLi7WVAgO5X5FRLELY+ZceHEFh0QOmsTH8Fl8tylKnwmMybiuQavPNwvNMJeTg/hHwD/5FlxgcJwe8ZSICLBfpH/ZXiJqxTplaA+HT4itPOszHxhlJbJO0yNHgzMGNmM6JZCYEACW3Jiujtin7ikGdboeM/C7mCSd4T/kdZ5KmAaWi7E/9cxNegMbW9tyvPmDrIBH1D7J+Ey/xERWxfLKfohGGIyn4t1KXkPeIfL1BgemcfgfkiCrvPLsl26fiP3eB/xHqU8siLaPUvaGnicRMuVr1LO0Q7MG4MF8kVx1hzLalbpct5Mp8c+sQDpmepPmBQUbvmPEpi23yVKmm/PmHXmxHi4du9XSQTaJop6rUZ3nwPELp2AWmd9Rhv8ASCurr1UDsBhP4g2W+tVN5D0vjkdfEv7nXH+412jUCHRkFOYl/iUy0PnQf7iBYAm9nn8Vtqtk/i+pcWOrP1BSNtf9auFG/Oao/dMsHzTn+yKYLsW/hitpNtX6jlg8v85fKMvEEQGtx37i24+IPap7xuO7V24r8wPJPN/ic2PYfUOonnf4ZbJHiGKqg2rI3tn8XUtRcDO+IXHm7G1KvzV5cQilerceR5Otwy93lm6JbbA8E59RqV8zPkMsUh61LyJ29ZiuqLi+eptGVtbaj8hbd3XN/wBTSYrGbNf55bXBC/PDgXMfpBxfxGNNvh0HU6AiCVib/X4TcgE0Jbx4P9ZlxexLgsbqF4tP4KWg+MSmx3k/zAwYND/J6+ZW/smlybL+oBaj3PsjgD7hGy4XWluYisDeI4JnwR/gd+IUaNC9HqDVYneeK1UPNZJVyvdcMqSnuifJMToPOnqICWrpzMFb1DPmfQ1la1nYlpHtkYiQcyGB6lfao43DNXXBWuRtW7K1vww2DBjxPM1oIfMIA2t4+YTHIPwh1ZR+3xwJ5zZGrJtzmojTpS4/dx2VNZWHiYu50wuxSjXNx3V8X9SrCc3fzuEpB3gB8kFK6B5Ip2mjbv8A1E+E8QQyTdv4w7++b/h7ifeINshmonuEBmB/9l2y5KDrrURCy9S8BTxUaYyus1DMcrBMs2VgNZdiwLogpHK4pgkTjJznuNLRTcL51sNwGG3n/M99FvEVcdxOSVOwdozMVjlxcRXB1iqPMtyrkr9cR3fqzDohc7n9wnWougpi3Y9E0ltK0iui+cb5uH3T48RbS7qrE7lOG4Wkz1wnbjm/4VD1aiuEwKrm0+CoyF4/77HjI6b9ETpburh4ErrlghrxguIwwLUBaibIemB5K6YT/Ll7A9MCZXgJc0r01mxL1zHa7mo2iP6hFQh3fkupy5Dz8eovrUwruFMpcsqNht6lUaqbWYUY8pEMszHgjuUwb1OGbUpraeDUuqAur3gEA/MzGsvk4LEVdlvdTJ5WIc8dS5u+GElBqenmD0qzvcOwFJzHAg5L4ILUl5bUubLr1+L+plvOavsEWPiNcvmZFa2Z/wCb43WOjX7cRdfsxNpC2L4Z4A4Kf5nIT23L6B1JY8CBiCDe4GyUuEp4nkQIx8IzpIJOIMap6ZqflzGYfjiVL2nfmAbZci8bGUMgttxCItDa4lmro0v+RavJ65YSko7ywPs/tf8A5CuhMq2sEB3eMcKs9VW4Rl7a/cuKphzV6jUY4cz4lvR6OHxGy4o4Y7zqCMNjVbl5VbV0S2xnCP7wQaivC0n1MH1yspvxPJvfJ9EBQAQ6tvS+ongKnn6iWq5K3xwWAKHHl1lP1E6OSon3nyQWkRKqf7Ko7ClqrlkZo9t8NB9jDhsywvx4+rC2E8iqjxj6iuOUKUyi5qwDkT2PkmJn9GEa/icsXBHhLhpM1LTVl7yRfEFO432PXc4Ijt0TOabq6IsEb9c3t4FwIaToSx7GaY1o28WRlanefbeZQ+2XELgOzN/cfQRpL58OL6uN+Csf3hhHKmNfxGAFFGEm6t0f1LmbYOL28TVheQ/vb8xHa/mn5vPqE6ostH1/69DK+o4XjofPglH4gRNGp+8JqX1FK9wmM/8AmgtF7p+fExolbWuP4+JcqoM3Qzwm/mVujXZX9k3ImMRdHkc/+YkogvP8wm3ubJT/ANlXpzS8aqeWR/mGQpfFqBhw5wbPiGpU8qSOZK9lR5GWFpYr2heXLQ2+IBy+4p4D6Ycn64JjBl9ZmMeTIs/USyTtZ2Z7sioEO2GL0x1mRsnTNOFl676VcRi4IN8wnu2KnEVU1dw3+oxHjbSYadcSfxGTvKcf3AAI3ihYeTAZ/cuu11fEYORXPeY+gfcJSzxOWYHLxs5+jt/8yqO/rf5vmBw0TR2+2PczbV7i9pazCS0O/KtgaPBGijY35jfUZ3r4nHi2/c4sw22XF0iCdzEaYqMCOSO3HG3mDquuZeQcVRBE7ld5KP8AIfHErYfsZXEdAwC222pMX+8E/wAQ9ODdRP0/1FMVdav5lzhG/wDLLtO+qn7jTvfifXqPZvFqHZszK8TKDrt5ZcWTijwY3myE2ITY0SvGzGKalZquTEJvSes/1KI7vnT0VK7qwXpnwErAIbULD5idXxV8u70ymn6Yyc03d4ijgq2D43Lq4Gg1Db2z8Sg1Xgf/ALiNOssTxRy/0eIUjd9cRINNoQIqaxqJ7jAiwHC8iHbNuu/GxUKO6SuRBd8fr/kttZdStnMWu+jvXJ2vTV8NwANl0yPInxURLaYxyoopw1LLGrhkwd4l7nHLJumU35mi1a8xnQDH/EY2UToVU2y0ahTpPPEvf7Y5efli20sXzmJI3W/zNxLqX8kFrjWT+YYSRnKx7JeKsb/0pAoS8A0fj3GlZJKGPmJy2NakY3o4j6zDO/xise1rv/yEBcca/mLcHAlbKo1RL9wpbXVm+gImLDeT9YBHuNf1KBXgARHfH71McwvKcvxLtN5Qlfx76mZqhqeI0GUDGYxuJgblWZGt7lw2c4/iErkGvcWB6lJFldK4qVwX47+JzBGsazqH2YRHt7A7XdNcwqqe4GwWL0JefqiHAmFBXV+xfmLGLEBMTfJXxua+rrphBjpx5IzAU04rbL5HmFb5yVDh41R+o0WBr8FxK6jaOPUziCzUsSlKfMeES65TsnDuY0esa/6YOC8zbCsjpzYgi7CvJ65hG2OHz4uCNHmi38wBg++P9QwuyzQfrML46LrsmDZAWUBClIM53C7K5g/qA1Dc4/8AyXyUM0o+DmLaYLszvVu5i/nzr51+pfwz1kIX/LQQMHl4lSFeJ6lY+EeVbW5cWduq1FIMdMqGBGsVYY3Nb3UWb2rGbDKyO51pnquYYK4lp6apyVxxF0m+Y5xXbZ7hmSt2lOV7hnMWmZlxFn989MxIt1h3BZG2cwiER2NVDmBLluA3OWrgMueVl4O3LPMozZvY7cYiLs8Y6X3MV5WmEqyTw+JdPXiBkhXHcbQ/i8wqhwGmD8fmMB33dv8AqFtFcYu3+Y4Cg46xAWwHXv3KyHZVv5i7oOCWjTkTedw1QfPMATWMsYdXuImTUs/cDQtTi/UA72iqof7hz563B/uHfgzH1GIx87jdMjuhKsLRzPnJqqblvgI17KbzL5KyrEB869QikN0aJaqbmoBE8I3uuoBQ6azU4jiVyy88Qd5yVkvmpcAnHQVNcY494cy94y7h1T6lM0FisKwW1ekYGX7DBRrVwMZT0rsT+5ybHkqLKl4xoff3EQC2mtPEsWQYuHLQ4RoNFLg+TFgTNabILT8iGyl6ee4nYi3Q6gX5NlG0ZUeLxpS1+oSJ0u4J5l9wJHpOpW0KrRrj3L9AOTz+ypRsUl1/uPCq+M6WFkQYtYyD/wD3UsFTgYge7mJmDyxqK8OrK03MePq4BTdWWviYQp3U/mH1vTqWk0OIwsKCVmVJmryR0+vMOILYIoDTUKaxbMFOn3KoE4mGPYudY1i4VyKoEQxjtiRuu4muxruFXuBLUbBejm/cPLf35OZTxRwJYsxVMMc8nMvFby4htqFvOB8Q01ntlLZznuM3d2bTF45brTyQhS17Llgw7qwqO8F11GXR17iMOA3MyqkpIEWyzZ1NNB0x9oauFkwfeQa+q48frUv4j3guFog6zFIDzSmVTzVWahfkKqv63OBnOCVLkNW8kYl+rD9deVqVXPc7/uCQRg4nwR5LGx/fHUoIgL1fiHRNFyvzG45tFGtufUeN1qJlrqYQr2zKa+iISVBjO4f0hFkYMniUpVk2TBQGanfMfqt3Vxwc6DxxLt2p7LceqzxvMYSto9Y7V7p1Lci27siel3KZivLUa5eala1Lw41Kt5G0h3bxjcyOvUpg7unMqgyeJa6jiUy+yHGnVl17xCtFXaGkljhYepA5Incq9XKldalBT5RolCHb9JKuqbmBO4enpvAj9rJpaf5Gloxxf4I9sEyn+UasG6tT/dR1Ql6uVsCeIROT5Wqj7hbNavjMWO6W8viPlve+Ys9DN9+I/O71lwayUOpzM+IUaXyxiu/NEbgUwBjA5EagAoP7wX5aggymKTCTCnvTiXK81jtNU1ChxtmCxgdjfDwb35+4Uta/OMqsHVYQ4aAZbxGtUuq5Zbw2qWEMA/cCm9blYcNV1BK6qqk7mOIqmoxsLzXUpJlOyNyRaxN9lUxFjjycz97QTFFs7cnXuVINMoYWMWyPcBwtHsRLalGMEVat8OJWujVF+4k4ByAfLMwDnBE/ctHEYLSAUtdahUBjpuVtqG3WMZxOXGPBAlfMyvcBwzVu5pXTRGztyt4m5bzM/RfEAC6hqe9R9rjABflrmGIHddRt2elYuI9ZhjSasZ81HiOodp1+oZKRTyXr7mhFart1/k5pPOhqRXjbKnoTJ6OmWnQaNW13CndmMTm2QVY7FYN+4+6FYrklDZo4E7ZPVR5+LpZ3n0PEVA85BmbZzaICuIoatf40c2nNbhe9dxFscTCDhmWyyNg//ZEKF01a+YXjaEH1L0FnBiXPj7Zjgjk7YxF4akzg6zMAfgu5cIvwxC6IhfDUQ9PuXdl9Sh5Ul/neIxDmV913K0D3VzGoAJRcCGMl9TA76jBdrMwC6uVo6VbGFq+8xxbbdDNVeodxglffyH/kuxXb1M68cQxOOBKK9RzLnwjCfQwBshFNI/cLq0LhYyFq9enzHYl0TBA87XGygKgTOZhbHx+vEpWU2KmXINqbE9QkVNxI/qU2HPmNVedPcbWm/D3Airg4qVuArLNdex/2GtqZjeIfM++4O72ShSgdxguA7laXox9zWBvg3KRpbvLmV1xfiMQL7lVWo6C1KGn3E6ilEneYikXxEJZYcRL4nG0Z9lQx0GP4xaA7WXE4uo2Q0J7zBfKJCcEw+IHiml88PwkKS5mzuBpMTCeYVy/x/MN7VXio4lgsTz1MQC0EQje+qqWoYWFraWTKGBYGEPqywAFqmEBDokysFuJLiRf71BjtzUplFlrvUOpt+orJSdy9LuWJM7gC5bd7iFKV26lN0PhmphIPd5rvFQtBtKKZXuc4nsXZxOAr4qM7/JgDaDjwgyYWo4G76RCZDQYcRXFHbuWzg+FXnmdgkqKeouoarR3ZHWONj4ZSed4mGocMAMdNy8M1t9Qu3VXiXKmjmZext+YW6rpqGrmH8QQ3RaWxWyYAvB/9mC+0qO6mOXxxClYNu2cL4lQ5xz+xJo0HUcCLXDsdSwVTkzKI013yTD0TmZOXpwkzHbkh6F+UoL5eNR3lZiyJvFMYPFgvEtLNt1GcGbriIkljhTxxCt58a1EoCvLBHQgGhzKXWOLXUPdXceeJcZmrjpJnG4Vgi7+JcZ2ifWM1LOGgtuJam3qbyxwGowO+oSnJSiTbOV+ZL9ysXHTk5l5q3dzj4rcKCkTSFGtkIacfzAm1h84hpQHWtS8QxvNUzEATYsNVCbjcYGdtyhTwAjHoatvUDWWnJ8QYsTT+8nGFFX2kZ2hru+wg5pYGlMb01NjdQhCnTKHIHmVVsc7tjECl86jJLJsWW5+xqNLC9fjeQt0j4jnt1OpS+SepQLMKI1YFL8xwiq89S5clcy5gTOVgyWsNkuA8o4lvEmKjRuKuTFxqYXzhr+fUdcHzDqB0k635xncVDCLEKrqxsprIOIDKaO5TZd6IM2HeY6llm6NkQHhvww5f1yt0V9QRW0S6iHCJ88wjXrKlF+pafBMDKi78QpJo4dn9wyN6Vlrti28XHFOLmJkAzg9Mv3I6b4ZVxpM2mHODXUa9Cl2Jd2x944Um4CccqPcTYi2+sbtpq7j7O8xxCtXmVOHvHMWuvLKKtazO4oeS4S9B1CTXxI6S/iKgIB/ZqO2NJxFCrr3LpuDd4mua6GJaS8PEN1NzOpEuXeIKQxXOGdcPUIQ5cNrEeg1rTzKrAKz7YYZ617sZYmTrxN0dW0SqCvmHbvX3CN3EKtoeZtjxHn58TKVDs6xFKeaKETSkGEjub0v5i9wO/Ii2Cu5cZBGCxlMb6jaUq1JllteIai1qZsMjEHhuYQVZcUSgDNl2S9PFxUktcFxYjlb7h2uPmK3Gbnl6tRBTCuy9kZcpnRmHJeV8StVZnEI70nMS1Di4qqo1Xmb485ivYwpHdJWyVyuIrSWL7i48nkrMtNjxMRY26iPMcxmxKY9X/wAhe6VZ8zMnBdKrMYc8tQ4o0t6lbcL0YcGW5ZFqc5Mcw5fuKnFJWAi2w2VqVaaL64nG8Y8wmVgXCtbLWVKVkEsl/odPEZ5SuUtbrNzULPDG3UbKaYEVsOSOGUUIkK3Lu7S7BmEvAXKAW8QcBd6l/C541Uw6HRLqMysTI4hEWdS4j4QAbSM+afUfgBvGKmh6t1Tcqp+sTma+eam6rPMph4AhUlRV6mKW9/8AY5MhMVK8W3xN4fI/EJ1vmW0JHfEqFqb5yAseF8QlKeKcwU0VriOEFbvKQWtxy4RHhdvE3VtT0bXyTn0UX0QMkexicVbSJw1OPi8wssurt8S7um9m2oh91Y/nCUgbvpjtEAwt5YbIVfCyumNGo3fMaMfEuCam33ExIGSs5lL9rW0b4DwQrINW9w6VoM+ZTrgJid5mypMVlu4DWSDRrhjRfAy2pBq2GwV4TFT2LM0BPErtHqX9Yux8S5FEq7Jfrf7qqPtgezZiYLaKpmoo1LrqarMSNDnFF8lHlCkTPXDLrWqyd4iUiCritJxM6bGFPuMq4vEkOEOHUcq1pHzmeTdLH16wu1YdCFVvmVogbOTmx6B4USQNUdtyaZmubZ5mrWGziLT44ZZFLVGw6iDKnk9Q1EUkoz08QnJwy2/HiCV7CUiEHqNKoG0Zm+rc9QwFUyjKFg7GpjZC6iOD2hv/ACN6PcyWaMzE1W2M4m+5gBjxD4AkugGUuEJWg/GcfUS3i+uoTNC6uFA3Bp3Hz5QGfmLb7XXiZimtVEW00zCyF7Fy1wLD3eoq7a69wtQ9ISr541MGKvfqHstq4TbnUF1kniIITDT0q+oUHHZerlAe7lPLFZ7HiWWRsXG9z47SC2jqzmW1Cr8U7jba0KufExTy+JWGnCdQgA4aF6i08xzOGY7GK1cOu5PrLJ8IM38ykUywF3iBEcGc3iYrhtjqGoBlLSeGcrDYxk8L0SoeRyBwRVAlpB3sYZyv+EF68qe7mAAi2d3Ct3XGODbUWs8xCre/qW6W/wDyNQFq/iMzl35ZkaYsw57glSoKlrhIPSqqtwCuFed9xdJ5jevOoDhwo2/eIBlrnXnmYmFA53sPcPKKAWDL/lUV+4T1OSDb1OA63ZLyMU3Kt4EKgYB5STfjFJa3Kh1FtpA33KHC7krKxvmGUlruW6rYxB4afjGkpDtlOGNZnxDLrzL4NOoQtB/mJYwhi9JieoEpCLeSXoI5JXTCvsxFy8QnVQnkoyP8wCDa4LjEHCcw7dFoZlXXRGqp02uOJi4le5bdngzQGi3QYxoMP/ErqStkc0KqHuG8Xd/mHS3Yy69Qy/UPIxNgDi+pnJ44vEqCBZGREds20C4lJSFy+vUySAs9LLIGx1nX4N7OGPCBAR7rDV+uYR3cGP6iKZFjXABfqWnMpHmhhgLfEqOSNXticqEZnrSfqc8CXrTmXNMe3FynwTL5jyGRL97ZdMGEovkuMEbbwMdyk5omYLwwRXZXkdSvnXTqZO2ZEhSkmDhmvouHNjHOcZUPZp4gI5xkFGI16xMdT6BmaZSQyyW1pmefEExgCauDqaVMtPm5IDhqbfXsjCdJwZjGOwLbuYq0wd5mZ5hTDlkVFc1A462p5jG9Gc9SkgYXZL8GNMqRgqAB2d6ZVcXFV6itm1lZRckZO+ZeQp0kqIFQC9lImV2ytUUh7G2qf8gWp8xUlQwxG6W94DEGcxK8MWSLIvmUGKl5tFzDbnHJKNBGUSLrYx7y8vLo8f6jfs2r+kzFMvaOxseY1PbLNiut2NwMCa2+cfCT1ucyzLfMEqqpsr2GMH+qDzZLCZpv5xbA3gMVI3nCiqaDh8MG02l6vi44k884ZhN6bO549W8vH8x4Vws8ezPLMLU02yKRuF9VA8rrWKBtMe5cFGv+mJxwrQ9Tgny3wRZiufuR/TvHEe6pt0Meh4z8yrZuKZmL4nOX+uoRIQX3ncNmUzha6uF0F4PggTicqDDCKPwwCxXcPHqVwGhlhlUtAc5ju+bVuYF6glYnqXYo1e5ZOHcw0/hcNKldeFhqWL2A98RlgBo6npirILcrEgA1xPi5ctC2vcpbVbvTDo2nHEdhnzErd1WnYYqceDDaqJHhYSwst6njfMroBCnDUYZ7rW81NXK8MBe0w+IuMjVXUq9NK4zZsLxaP9RhEXbOdpiyFlbrOJQOwZ1bL/v9fuJaIfcKvIq5ZqHZEOWXv+ULkIAR1BZfVsMBfUCoIr3/ABvXZ5gVXcxhvPcILHq4fBCSwd/6jRKP252WzTniDOT4cRWxOTX6hOP4SVYbjQ4ZnyRVwWbgwS1txEvOPEycrSnDLfKIfIyjMr0eYxbkOpcVRRIe/NPQYI+ROIw1dbj2EtHsZmnuvENkOq5PljrqE0Kf2MTIe9XhhwilFkqTi1R+Id0v3BQKBe9MrwoVbyTVOHom1moyTfK8E2zGkCrwf9lBpxAnBg6yy8k6AG5gHiYvZiDJmHPL/iFmAK+IbZmQqLJepXQF6gVcjb1OZrxBtNNysUWWYLYwtL3ZrwEuTrpt1QfqMvMD5jFpuiypALTXMPUI6mVmUivCWf8AIBVOm+xmPRM83w8ypLe0UbhjVHLXNwWL18nwxsROnMPqOJve4XE0UioK7l4V05iWjPGIGMb0OYasoQfcFxnr1L9KwEmu4wVhMnVRYjPR1ctJRkPOcTwvLMYRSKdLn47jVdIt1VxN2htVmP6b7lboRwE0gbtzMUaXuXnNmgqEhROrZeJ4Y0PeyyrYG4MYzcpwu++pwkb9SpTa4DnC1QrL6jMLuTUyAaaeguPjV4N8zkG+JM7Mw+MbrAUqvMukUT1DzwtCJwFcrg9xvNbbe5eHY6iRWy2BDkjfWX2VKCtC4vzHokL2eZhJUpq6iva69bhuGqXH6jV3qZWIAtHJqBAbJs2w9SUHGjUc/A1iU+arWqmCZeEb+SW5aUbqYuqpcM1d/LxYfd7qumWFJdMcoxVYlACnDyf8l3nsZmShd30e2O85l/z4l/OzQTnr3frgi1apu2GHTPvMs+YrV6jiayt9IZ0YepjVzUGgJ5IXCrhseviavKxxs3MlQbK/xCIP2l/NDh7df7At1pw0vMNYVvcKscZxZBq7u+iAydF95e0YS1ZwepnSri6leW4l2NnmFzKmajbajxL4q6I7mKo9MGXf0rqOxiyn+kPxGkvyMua9XJGLYwunMsLu26hAUtFgdxmjp4wvW4soJYlZLubIXRFjxpTGFXfuXVa3jl9+Y9Qh1KtY1zBah7CXs8BP/9k="
@app.route('/seam/',methods=['POST'])
def removeseam():
    request_data = request.get_json()
    imageURI = request_data["imgData"]
    seams = request_data["seams"]
    print(seams)

    result = seamcarve2.reduce_seams(imageURI,seams)

    # f = open('image.txt','a')
    # f.write(result)
    return result



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105,debug=True)