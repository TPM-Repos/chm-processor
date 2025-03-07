Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EagerLoadResources Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewResourceHandler Interface](topic7286.md) : EagerLoadResources Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Begins loading resources from the preview so that GetPreviewResource returns results quicker. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function EagerLoadResources() As Task  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewResourceHandler](topic7286.md)
    Dim value As Task
     
    value = instance.EagerLoadResources()  
  
C#|   
---|---  
      
    
    Task EagerLoadResources()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewResourceHandler Interface](topic7286.md)   
[IPreviewResourceHandler Members](topic7287.md)


