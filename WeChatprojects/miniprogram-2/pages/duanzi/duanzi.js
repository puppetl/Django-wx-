// pages/duanzi/duanzi.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var timestamp = Date.parse(new Date())/1000;
    wx.request({
      
      url: 'http://v.juhe.cn/joke/content/list.php?sort=desc&page=4&pagesize=20&time=' + timestamp + '&key=0bc33fd508311bd135a3e2f19f7d0d99',

      header: {

        'content-type': 'application/json'

      },

      success: res => {

        //1:在控制台打印一下返回的res.data数据

        console.log('successs request ok!' + res.data)
        console.log('time----->', timestamp)

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