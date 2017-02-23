function assetdel_confirmd(id,name){
    var url = '/assetmanage/asset_del/'+id;
    var msg="确定要删除资产"+ name +"吗？"
    if (confirm(msg)){
        window.location.href= url;
        // return true;
    }else{
        //console.log('false')
        return false;
    }
}


function groupdel_confirmd(id,name){
    var url = '/accounts/groupdel/'+id;
    var msg="确定要删除组"+ name +"吗？"
    if (confirm(msg)){
        window.location.href= url;
        // return true;
    }else{
        //console.log('false')
        return false;
    }
}

function userdel_confirmd(id,name){
    var url = '/accounts/userdel/'+id;
    var msg="确定要删除用户"+ name +"吗？"
    if (confirm(msg)){
        window.location.href= url;
        // return true;
    }else{
        //console.log('false')
        return false;
    }
}

function minion_delete(){   
    var selVal = $('#accepted option:selected').val();
    var msg="确定要删除"+ selVal +"吗？"

    if (selVal){
        if(confirm(msg)){
            document.getElementById("minion").submit();
        }
        else{
            return false;
        }
    }
}


function accept_reject(){
    
    var selVal = $('#s_accept_reject option:selected').val();
    var msg="确定要删除"+ selVal +"吗？"

    if (selVal){
        if (confirm(msg)){
            document.getElementById("f_accept_reject").submit();
        }
    }
    else{
            return false;
        }
}
