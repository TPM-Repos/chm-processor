![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertTableToDouble(Object,CultureInfo) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9569.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [ConvertTableToDouble Method](topic9567.md) : ConvertTableToDouble(Object,CultureInfo) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The source value.

_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

Glossary Item Box

Converts a table to a double. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function ConvertTableToDouble( _
       ByVal _value_ As Object, _
       ByVal _culture_ As CultureInfo _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As Object
    Dim culture As CultureInfo
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertTableToDouble(value, culture)  
  
C#|   
---|---  
      
    
    public static object ConvertTableToDouble( 
       object _value_ ,
       CultureInfo _culture_
    )  
  
#### Parameters

 _value_
    The source value.
_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

#### Return Value

A table.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9567.md)

©2024 DriveWorks Ltd. All Rights Reserved.
