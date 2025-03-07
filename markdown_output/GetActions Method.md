Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetActions Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupProcess Class](topic9776.md) : GetActions Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all actions. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetActions() As IEnumerable(Of ProcessActionBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupProcess](topic9776.md)
    Dim value As IEnumerable(Of ProcessActionBase)
     
    value = instance.GetActions()  
  
C#|   
---|---  
      
    
    public IEnumerable<ProcessActionBase> GetActions()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupProcess Class](topic9776.md)   
[CopyGroupProcess Members](topic9777.md)


