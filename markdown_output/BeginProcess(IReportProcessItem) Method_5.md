Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(IReportProcessItem) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportWriterBase Class](topic10476.md) > [BeginProcess Method](topic10483.md) : BeginProcess(IReportProcessItem) Method  
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
      
    
    Public Overloads Overridable Sub BeginProcess( _
       ByVal _processItem_ As [IReportProcessItem](topic2285.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportWriterBase](topic10476.md)
    Dim processItem As [IReportProcessItem](topic2285.md)
     
    instance.BeginProcess(processItem)  
  
C#|   
---|---  
      
    
    public virtual void BeginProcess( 
       [IReportProcessItem](topic2285.md) _processItem_
    )  
  
#### Parameters

 _processItem_
    The process item to use to begin this process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportWriterBase Class](topic10476.md)   
[ReportWriterBase Members](topic10477.md)   
[Overload List](topic10483.md)


