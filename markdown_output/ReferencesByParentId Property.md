![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReferencesByParentId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleasedComponentReferenceTree Interface](topic6106.md) : ReferencesByParentId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a map from a parent component's identifier to the references for that component. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ReferencesByParentId As IDictionary(Of Guid,IEnumerable(Of ReleasedComponentReferenceDetails))  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleasedComponentReferenceTree](topic6106.md)
    Dim value As IDictionary(Of Guid,IEnumerable(Of ReleasedComponentReferenceDetails))
     
    value = instance.ReferencesByParentId  
  
C#|   
---|---  
      
    
    IDictionary<Guid,IEnumerable<ReleasedComponentReferenceDetails>> ReferencesByParentId {get;}  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleasedComponentReferenceTree Interface](topic6106.md)   
[IReleasedComponentReferenceTree Members](topic6107.md)


