import React,{useState,useRef} from 'react';
import { useRoute } from '@react-navigation/native';
import { StyleSheet, Text, View ,TextInput,TouchableOpacity} from 'react-native';
import {Timer, Countdown} from 'react-native-element-timer';
import { useEffect } from 'react';
import { url } from '../../baseUrl';
import axios from 'axios';

function Verification({navigation}) {

    const[first,setFirst]=useState('')
    const[second,setSecond]=useState('')
    const[third,setThird]=useState('')
    const[fourth,setFourth]=useState('')


    const[err,setErr]=useState('');
    const route=useRoute();


    useEffect(()=>{
        axios.post(`${url}/auth/sendotp`,{
            'email':route.params.email,
            'type':'authenticated'
        })
        .catch(function (error) {
            console.log(error);
        });
    },[])

    const press=()=>{
        axios.post(`${url}/auth/resetpassword`,{
            'email':route.params.email,
            'password':route.params.password,
            'f':first,
            's':second,
            't':third,
            'fo':fourth,
            
        })
        .then(function (response) {
          console.log(response)
            if(response['data']['status']===200){
            navigation.navigate('Login',{
              msgs:"New Password Created!"
            })
            }
            else if(response['data']['msg']==='max trying limit exceed'){
              navigation.navigate('Login',{
                  err:'max trying limit exceed'
                })
          }
            else{
              setErr(response['data']['msg'])
            }
        })
        .catch(function (error) {
            console.log(error);
        });
    }


  return (
    <>
      <View style={styles.container}>
        <View style={{width:'80%'}}>
        <Text style={{fontWeight:'bold',fontSize:20,marginTop:50}}>Enter your OTP that you receive in your registered email.</Text>
        </View>
      
        <View style={styles.fields}>
        <TextInput keyboardType="number-pad" style={{height:50,width:50,borderColor:'black',borderWidth:1,display:'flex',justifyContent:'center',alignItems:'center'}} value={first} onChangeText={(b)=>{first.length<1&&setFirst(b)}} />
            <TextInput keyboardType="number-pad" style={{height:50,width:50,borderColor:'black',borderWidth:1,display:'flex',justifyContent:'center',alignItems:'center'}} value={second} onChangeText={(b)=>{second.length<1&&setSecond(b)}} />
            <TextInput keyboardType="number-pad" style={{height:50,width:50,borderColor:'black',borderWidth:1,display:'flex',justifyContent:'center',alignItems:'center'}} value={third} onChangeText={(b)=>{third.length<1&&setThird(b)}} />
            <TextInput keyboardType="number-pad" style={{height:50,width:50,borderColor:'black',borderWidth:1,display:'flex',justifyContent:'center',alignItems:'center'}} value={fourth} onChangeText={(b)=>{fourth.length<1&&setFourth(b)}} />
        </View>
        {err&&<Text style={{fontWeight:'bold',color:'red',marginTop:15}}>{err}</Text>}
        <TouchableOpacity style={styles.btn} onPress={press}>
          <Text style={{color:'white'}}>Send</Text>
      </TouchableOpacity>
      </View>
    </>
  )
}

const styles = StyleSheet.create({
    container: {
      backgroundColor: 'white',
      height:'100%',
      width:'100%',
      display:'flex',
      alignItems:'center'
    },
    fields:{
        width:'70%',
        display:'flex',
        flexDirection:'row',
        justifyContent:'space-around',
        alignItems:'center',
        height:90,
        marginTop:150
    },
    btn:{
        width:'70%',
        height:33,
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        backgroundColor:'blue',
        marginTop:50
      }
})

export default Verification