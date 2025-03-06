![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetChildSpecificationDetails Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : GetChildSpecificationDetails Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationName_
    The name of the specification to get the details of.

Glossary Item Box

Gets the specification details for the specification name provided. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetChildSpecificationDetails( _
       ByVal _specificationName_ As String _
    ) As [SpecificationDetails](topic11292.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim specificationName As String
    Dim value As [SpecificationDetails](topic11292.md)
     
    value = instance.GetChildSpecificationDetails(specificationName)  
  
C#|   
---|---  
      
    
    public [SpecificationDetails](topic11292.md) GetChildSpecificationDetails( 
       string _specificationName_
    )  
  
#### Parameters

 _specificationName_
    The name of the specification to get the details of.

#### Return Value

The found specification Details or a null if not found.

# ![](dotnetimages/collapse.gif)Remarks

This is the only way to get specification details for embedded specifications.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


