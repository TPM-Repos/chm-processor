Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Applicator Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [PendingChange Class](topic882.md) : Applicator Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a method that will resolve this pending change (save it). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Applicator As Action  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PendingChange](topic882.md)
    Dim value As Action
     
    value = instance.Applicator  
  
C#|   
---|---  
      
    
    public Action Applicator {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PendingChange Class](topic882.md)   
[PendingChange Members](topic883.md)


