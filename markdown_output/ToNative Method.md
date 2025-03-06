![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ToNative Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9378.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [IPropertyValueConverter Interface](topic9373.md) : ToNative Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value from the backing store.

Glossary Item Box

Takes the value from the backing store and converts it to its native type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ToNative( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPropertyValueConverter](topic9373.md)
    Dim value As Object
    Dim value As Object
     
    value = instance.ToNative(value)  
  
C#|   
---|---  
      
    
    object ToNative( 
       object _value_
    )  
  
#### Parameters

 _value_
    The value from the backing store.

#### Return Value

A value of the native type.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPropertyValueConverter Interface](topic9373.md)   
[IPropertyValueConverter Members](topic9374.md)

©2024 DriveWorks Ltd. All Rights Reserved.
