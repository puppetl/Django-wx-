// pages/apps/apps.js
const app = getApp()
Page({
  data: {
    grids: [0, 1, 2, 3, 4, 5, 6, 7, 8]
  },
  onNavigatorTap: function(e){
    console.log(e)
    var index = e.currentTarget.dataset.index
    wx.showToast({
      title: 'index+',
    })
    var item = this.data.grids[index]
    wx.showToast({
      title: item.app.name,
    })
    if (item.app.name=='支付宝'){
      wx.navigateTo({
        url: '/pages/zfb/zfb',
      })

    } else if (item.app.name=='微信'){
      wx.navigateTo({
        url: '/pages/wx1/wx1',
      })
    } 
    else if (item.app.name == '新闻头条') {
      wx.navigateTo({
        url: '/pages/news/news',
      })
    }
    else if (item.app.name == '精品段子') {
      wx.navigateTo({
        url: '/pages/duanzi/duanzi',
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.updateMenuDate()
  },
  updateMenuDate: function(){
    var appnames = this
    // 后台获取数据
    wx.request({
      // url: 'http://127.0.0.1:8000/api/v1.0/jokes/apps/',
      url: app.globalData.appurl + app.globalData.appv + app.globalData.routeapp,
      success: function(res){
        // 更新数据
        console.log('request ok!')
        console.log(res.data)
        appnames.setData({grids: res.data.publish})
      },
      fail: function(res){
        console.log(res.errMsg)
        console.log(this.url)
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