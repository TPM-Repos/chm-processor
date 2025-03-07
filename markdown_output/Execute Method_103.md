Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [AddGroupUserToTeamAction Class](topic9643.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_report_
    A method that can be used for reporting status.

Glossary Item Box

Executes this action. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function Execute( _
       ByVal _report_ As [ReportMethod](topic10006.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AddGroupUserToTeamAction](topic9643.md)
    Dim report As [ReportMethod](topic10006.md)
    Dim value As Boolean
     
    value = instance.Execute(report)  
  
C#|   
---|---  
      
    
    public override bool Execute( 
       [ReportMethod](topic10006.md) _report_
    )  
  
#### Parameters

 _report_
    A method that can be used for reporting status.

#### Return Value

False if there is a critical error that means the entire transfer process should end.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AddGroupUserToTeamAction Class](topic9643.md)   
[AddGroupUserToTeamAction Members](topic9644.md)


