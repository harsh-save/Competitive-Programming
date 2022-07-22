const mergeArray=(nums1,m,nums2,n)=>{
    let sortedArray=[]
    for(let i=0;i<m+n;i++){
        if(nums1[i] && nums2[i]){
            if(nums1[i]>=nums2[i]){
                sortedArray.push(nums2[i])
                sortedArray.push(nums1[i])
        }
        if (nums1[i]<=nums2[i]){
                sortedArray.push(nums1[i])
                sortedArray.push(nums2[i])
        }
    }
}
return sortedArray
}

console.log(mergeArray([1,2,3,0,0,0],3,[2,5,6],3))