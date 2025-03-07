Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DependentActions Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [ProcessActionBase Class](topic9935.md) : DependentActions Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

All actions that are required to have executed for this action to run. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property DependentActions As List(Of ProcessActionBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProcessActionBase](topic9935.md)
    Dim value As List(Of ProcessActionBase)
     
    value = instance.DependentActions  
  
C#|   
---|---  
      
    
    public List<ProcessActionBase> DependentActions {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProcessActionBase Class](topic9935.md)   
[ProcessActionBase Members](topic9936.md)


