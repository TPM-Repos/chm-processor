Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [CapturedComponentStatus Class](topic2459.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifier of the captured component if it exists, otherwise a null reference is returned. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Id As Nullable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedComponentStatus](topic2459.md)
    Dim value As Nullable(Of Guid)
     
    value = instance.Id  
  
C#|   
---|---  
      
    
    public Nullable<Guid> Id {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedComponentStatus Class](topic2459.md)   
[CapturedComponentStatus Members](topic2460.md)


