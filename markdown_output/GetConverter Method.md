![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConverter Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9406.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : GetConverter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_clrType_
    The CLR type for which to get a property value converter.

_throwOnError_
    True to throw an System.ArgumentOutOfRangeException if no converter is found, otherwise false.

Glossary Item Box

Gets the property value converter for the given CLR type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetConverter( _
       ByVal _clrType_ As Type, _
       ByVal _throwOnError_ As Boolean _
    ) As [IPropertyValueConverter](topic9373.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim clrType As Type
    Dim throwOnError As Boolean
    Dim value As [IPropertyValueConverter](topic9373.md)
     
    value = [DynamicProperty](topic9398.md).GetConverter(clrType, throwOnError)  
  
C#|   
---|---  
      
    
    public static [IPropertyValueConverter](topic9373.md) GetConverter( 
       Type _clrType_ ,
       bool _throwOnError_
    )  
  
#### Parameters

 _clrType_
    The CLR type for which to get a property value converter.
_throwOnError_
    True to throw an System.ArgumentOutOfRangeException if no converter is found, otherwise false.

#### Return Value

The property value converter for the given CLR type, or a null reference if none is found and throwOnError is false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)

©2024 DriveWorks Ltd. All Rights Reserved.
