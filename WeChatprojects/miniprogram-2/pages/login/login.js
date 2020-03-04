// pages/login/login.js
const app = getApp()
const cookieUtil = require('../../utils/util.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cookie:[],
    isLogin: null,
    userInfo: null,
    hasUserInfo: null
  },
  getCookie:function(){
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/blog/cookietest',
      success: function(res){
        // 获取cookie
        var cookie = cookieUtil.getSessionIDFromResponse(res)
        // console.log(cookie)
        // 保存本地
        cookieUtil.setCookieToStorage(cookie)
        that.setData({
          cookie: cookie,
        })
      }
    })
  },
  sendCookie: function(){
    var newcookie = cookieUtil.getCookieFromStorage()
    var header={}
    header.Cookie = newcookie
    wx.request({
      url: 'http://127.0.0.1:8000/blog/cookieaccept',
      header: header,
      success: function(res){
        console.log(res)
      }
    })
  },
  authorize: function(){
    var that = this

    wx.login({
      success: function(res){
        wx.request({
          url: 'http://127.0.0.1:8000/blog/authorize',
          method: 'POST',
          data: {
            code: res.code,
            nickname: app.globalData.userInfo.nickName
          },
          success:function(res){
            wx.showToast({
              title: '认证成功',
            })
            var cookie = cookieUtil.getSessionIDFromResponse(res)
            console.log(cookie)
            cookieUtil.setCookieToStorage(cookie)
            that.setData({
              isLogin: true,
              userInfo: app.globalData.userInfo,
              hasUserInfo: true
            })
            app.setAuthStatus(true)
          }
        })
      }
    })
  },
  logout:function(){
    var that = this
    var cookie = cookieUtil.getCookieFromStorage()
    var header = {}
    header.Cookie = cookie
    wx.request({
      url: 'http://127.0.0.1:8000/blog/logout',
      method: 'GET',
      header: header,
      success: function(res){
        that.setData({
          isLogin: false,
          userInfo: null,
          hasUserInfo: false
        })
        cookieUtil.setCookieToStorage('')
        app.setAuthStatus(false)
      }
    })

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