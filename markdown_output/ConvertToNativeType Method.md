![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertToNativeType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty Class](topic10946.md) : ConvertToNativeType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_obj_
    The object to convert.

Glossary Item Box

Takes the given object and converts it into the native type of the property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function ConvertToNativeType( _
       ByVal _obj_ As Object _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty](topic10946.md)
    Dim obj As Object
    Dim value As Object
     
    value = instance.ConvertToNativeType(obj)  
  
C#|   
---|---  
      
    
    public abstract object ConvertToNativeType( 
       object _obj_
    )  
  
#### Parameters

 _obj_
    The object to convert.

#### Return Value

The object converted into the type of this property.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[UnparsableFlowPropertyValueException](topic11805.md)| Thrown when the value cannot be converted into this property's type.  
  
# ![](dotnetimages/collapse.gif)Remarks

This takes any value, and converts it to a type suitable to pass into [SetValue](topic10963.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowProperty Class](topic10946.md)   
[FlowProperty Members](topic10947.md)


