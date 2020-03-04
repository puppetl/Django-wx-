// pages/jokes/jokes.js
Page({

  data: {

    list: [],

  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({

      //获取头条新闻(type=top，新闻类型根据自己需求填写,top(头条),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)，我这里选的top)

      url: 'http://v.juhe.cn/toutiao/index?type=top&key=95aec0e79cd165df427c309572ceeb3e',

      header: {

        'content-type': 'application/json'

      },

      success: res => {

        //1:在控制台打印一下返回的res.data数据

        console.log(res.data)

        //2:在请求接口成功之后，用setData接收数据

        this.setData({

          //第一个data为固定用法，第二个data是json中的data

          list: res.data.result.data

        })

      }

    })




  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {



  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})