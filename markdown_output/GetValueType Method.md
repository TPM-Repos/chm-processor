![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetValueType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) : GetValueType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value whose type is to be determined.

_throwOnError_
    

Glossary Item Box

Gets the store value type for the specified value. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetValueType( _
       ByVal _value_ As Object, _
       ByVal _throwOnError_ As Boolean _
    ) As [StoreValueType](topic7322.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As Object
    Dim throwOnError As Boolean
    Dim value As [StoreValueType](topic7322.md)
     
    value = [StoreConverter](topic9528.md).GetValueType(value, throwOnError)  
  
C#|   
---|---  
      
    
    public static [StoreValueType](topic7322.md) GetValueType( 
       object _value_ ,
       bool _throwOnError_
    )  
  
#### Parameters

 _value_
    The value whose type is to be determined.
_throwOnError_
    

#### Return Value

The store value type of the specified value.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)


