Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentGeneration Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : DocumentGeneration Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets when documents are generated using the default specification flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DocumentGeneration As [DocumentGenerationOptions](topic10768.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As [DocumentGenerationOptions](topic10768.md)
     
    instance.DocumentGeneration = value
     
    value = instance.DocumentGeneration  
  
C#|   
---|---  
      
    
    public [DocumentGenerationOptions](topic10768.md) DocumentGeneration {get; set;}  
  
# Remarks

This setting is defined for the default specification-flow which uses it to determine whether to generate documents during the finish process, or release process, or both.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)


