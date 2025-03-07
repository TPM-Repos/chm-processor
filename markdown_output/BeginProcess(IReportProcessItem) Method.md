Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(IReportProcessItem) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [IReportWriter Interface](topic10344.md) > [BeginProcess Method](topic10349.md) : BeginProcess(IReportProcessItem) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_processItem_
    The [DriveWorks.IReportProcessItem](topic2285.md) to use to begin the process.

Glossary Item Box

Begins a process using a IReleaseProcessItem structure. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub BeginProcess( _
       ByVal _processItem_ As [IReportProcessItem](topic2285.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReportWriter](topic10344.md)
    Dim processItem As [IReportProcessItem](topic2285.md)
     
    instance.BeginProcess(processItem)  
  
C#|   
---|---  
      
    
    void BeginProcess( 
       [IReportProcessItem](topic2285.md) _processItem_
    )  
  
#### Parameters

 _processItem_
    The [DriveWorks.IReportProcessItem](topic2285.md) to use to begin the process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReportWriter Interface](topic10344.md)   
[IReportWriter Members](topic10345.md)   
[Overload List](topic10349.md)


