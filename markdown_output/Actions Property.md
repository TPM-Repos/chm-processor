Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Actions Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupProcess Class](topic9776.md) : Actions Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The current actions to be executed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected ReadOnly Property Actions As Queue(Of ProcessActionBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupProcess](topic9776.md)
    Dim value As Queue(Of ProcessActionBase)
     
    value = instance.Actions  
  
C#|   
---|---  
      
    
    protected Queue<ProcessActionBase> Actions {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupProcess Class](topic9776.md)   
[CopyGroupProcess Members](topic9777.md)


