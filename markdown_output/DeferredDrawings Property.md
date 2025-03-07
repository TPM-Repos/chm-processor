Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeferredDrawings Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [ReleaseModelsTask Class](topic12489.md) : DeferredDrawings Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the identifiers of the drawings to flag for generation at a later stage, where "*" is a special identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DeferredDrawings As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseModelsTask](topic12489.md)
    Dim value As String
     
    instance.DeferredDrawings = value
     
    value = instance.DeferredDrawings  
  
C#|   
---|---  
      
    
    public string DeferredDrawings {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseModelsTask Class](topic12489.md)   
[ReleaseModelsTask Members](topic12490.md)


