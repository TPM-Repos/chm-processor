![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(XElement) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) > [Load Method](topic11143.md) : Load(XElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_element_
    The RuleResults element from which to load results.

Glossary Item Box

Loads the rule results for the specified XML element which must have the name RuleResults in the specification namespace (http://schemas.driveworks.co.uk/specification/) 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Load( _
       ByVal _element_ As XElement _
    ) As [RuleResults](topic11136.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim element As XElement
    Dim value As [RuleResults](topic11136.md)
     
    value = [RuleResults](topic11136.md).Load(element)  
  
C#|   
---|---  
      
    
    public static [RuleResults](topic11136.md) Load( 
       XElement _element_
    )  
  
#### Parameters

 _element_
    The RuleResults element from which to load results.

#### Return Value

An instance of the [RuleResults](topic11136.md) type which has been populated with the rule results from the serialized XML, or a null reference if the input element is not a RuleResults element.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)   
[Overload List](topic11143.md)


