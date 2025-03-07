Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetExternalReferencePaths Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IHasReferences Interface](topic6099.md) : GetExternalReferencePaths Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all references paths that this object has. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetExternalReferencePaths() As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasReferences](topic6099.md)
    Dim value() As String
     
    value = instance.GetExternalReferencePaths()  
  
C#|   
---|---  
      
    
    string[] GetExternalReferencePaths()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasReferences Interface](topic6099.md)   
[IHasReferences Members](topic6100.md)


