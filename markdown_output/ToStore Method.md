![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ToStore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9379.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [IPropertyValueConverter Interface](topic9373.md) : ToStore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The native value to convert.

Glossary Item Box

Takes a native value, and converts it to one of the types understood by the backing store. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ToStore( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPropertyValueConverter](topic9373.md)
    Dim value As Object
    Dim value As Object
     
    value = instance.ToStore(value)  
  
C#|   
---|---  
      
    
    object ToStore( 
       object _value_
    )  
  
#### Parameters

 _value_
    The native value to convert.

#### Return Value

A value in one of the types understood by the backing store.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPropertyValueConverter Interface](topic9373.md)   
[IPropertyValueConverter Members](topic9374.md)

©2024 DriveWorks Ltd. All Rights Reserved.
