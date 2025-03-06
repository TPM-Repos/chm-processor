![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Convert(Object,StoreValueType,StoreValueType) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9537.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [Convert Method](topic9534.md) : Convert(Object,StoreValueType,StoreValueType) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

_sourceType_
    The source type of the value.

_destinationType_
    The destination type.

Glossary Item Box

Converts the specified value from its current type to the specified type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Convert( _
       ByVal _value_ As Object, _
       ByVal _sourceType_ As [StoreValueType](topic7322.md), _
       ByVal _destinationType_ As [StoreValueType](topic7322.md) _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As Object
    Dim sourceType As [StoreValueType](topic7322.md)
    Dim destinationType As [StoreValueType](topic7322.md)
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).Convert(value, sourceType, destinationType)  
  
C#|   
---|---  
      
    
    public static object Convert( 
       object _value_ ,
       [StoreValueType](topic7322.md) _sourceType_ ,
       [StoreValueType](topic7322.md) _destinationType_
    )  
  
#### Parameters

 _value_
    The value to convert.
_sourceType_
    The source type of the value.
_destinationType_
    The destination type.

#### Return Value

The converted value.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9534.md)

©2024 DriveWorks Ltd. All Rights Reserved.
