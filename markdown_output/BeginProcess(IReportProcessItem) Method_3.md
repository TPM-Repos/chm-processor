Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(IReportProcessItem) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [EventReportWriter Class](topic10409.md) > [BeginProcess Method](topic10416.md) : BeginProcess(IReportProcessItem) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_processItem_
    The process item to use to begin this process.

Glossary Item Box

Begins a process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overrides Sub BeginProcess( _
       ByVal _processItem_ As [IReportProcessItem](topic2285.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [EventReportWriter](topic10409.md)
    Dim processItem As [IReportProcessItem](topic2285.md)
     
    instance.BeginProcess(processItem)  
  
C#|   
---|---  
      
    
    public override void BeginProcess( 
       [IReportProcessItem](topic2285.md) _processItem_
    )  
  
#### Parameters

 _processItem_
    The process item to use to begin this process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EventReportWriter Class](topic10409.md)   
[EventReportWriter Members](topic10410.md)   
[Overload List](topic10416.md)


