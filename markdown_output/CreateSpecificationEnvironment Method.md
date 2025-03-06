![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateSpecificationEnvironment Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationFactory Interface](topic471.md) : CreateSpecificationEnvironment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates the default specification environment for the application. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateSpecificationEnvironment() As [SpecificationEnvironment](topic11355.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFactory](topic471.md)
    Dim value As [SpecificationEnvironment](topic11355.md)
     
    value = instance.CreateSpecificationEnvironment()  
  
C#|   
---|---  
      
    
    [SpecificationEnvironment](topic11355.md) CreateSpecificationEnvironment()  
  
# ![](dotnetimages/collapse.gif)Remarks

The returned specification environment may be locked from further changes.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationFactory Interface](topic471.md)   
[ISpecificationFactory Members](topic472.md)


