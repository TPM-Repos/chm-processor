![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Convert(Object,StoreValueType,CultureInfo) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9536.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [Convert Method](topic9534.md) : Convert(Object,StoreValueType,CultureInfo) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

_destinationType_
    The destination type.

_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

Glossary Item Box

Converts the specified value from its current type to the specified type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Convert( _
       ByVal _value_ As Object, _
       ByVal _destinationType_ As [StoreValueType](topic7322.md), _
       ByVal _culture_ As CultureInfo _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As Object
    Dim destinationType As [StoreValueType](topic7322.md)
    Dim culture As CultureInfo
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).Convert(value, destinationType, culture)  
  
C#|   
---|---  
      
    
    public static object Convert( 
       object _value_ ,
       [StoreValueType](topic7322.md) _destinationType_ ,
       CultureInfo _culture_
    )  
  
#### Parameters

 _value_
    The value to convert.
_destinationType_
    The destination type.
_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

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
