// pages/ceshi/ceshi.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    array: [{ msg: app.globalData.abc }, { msg: '列表第二项' }],
  },
  dianji: function () {
    console.log('点击触发事件')
    this.setData({ motto: '你好,世界' })
  },
  changan: function () {
    console.log('长按触发事件')
  },
  tnr: function () {
    wx.request({
      url: 'http://v.juhe.cn/joke/content/list.php?sort=1234567899&page=3&pagesize=4&time=1418816972&key=0bc33fd508311bd135a3e2f19f7d0d99',
      method: 'GET',
      header: {},
      success:function(res){
        console.log('结果success:' + res.content)
      },
      fail:function(res){
        console.log('结果fail:' + res.errMsg)

      }
    })
  },
  save_cash: function(){
    console.log('save cash ok!')

    wx.setStorage({
      key: 'text',
      data: 'cash data save',
    })
  },
  read_cash: function(){
    wx.getStorage({
      key: 'text',
      success: function(res) {
        console.log('read cash ok--->data: ' + res.data)
      },
      fail: function(res){
        console.log('read cash fail--->' + res.errMsg)
      }
    })
  },
  remove_cash: function(){
    wx.removeStorage({
      key: 'text',
      success: function(res) {
        console.log('remove cash key ok!')
      },
    })
  },
  clear_cash: function(){
    wx.clearStorage()
    console.log('clera cash all key ok!')
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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