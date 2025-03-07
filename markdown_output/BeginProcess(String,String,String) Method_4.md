Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(String,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ProxyReportWriter Class](topic10434.md) > [BeginProcess Method](topic10443.md) : BeginProcess(String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_processClass_
    The class of the process, e.g. "Drive Dimensions", useful for filtering.

_processTarget_
    The target of the process, e.g. "SomePart.sldprt", useful for filtering.

_processDescription_
    The human-readable description of the process, e.g. "Driving dimensions in part 'SomePart.sldprt'".

Glossary Item Box

Begins a process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overridable Sub BeginProcess( _
       ByVal _processClass_ As String, _
       ByVal _processTarget_ As String, _
       ByVal _processDescription_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProxyReportWriter](topic10434.md)
    Dim processClass As String
    Dim processTarget As String
    Dim processDescription As String
     
    instance.BeginProcess(processClass, processTarget, processDescription)  
  
C#|   
---|---  
      
    
    public virtual void BeginProcess( 
       string _processClass_ ,
       string _processTarget_ ,
       string _processDescription_
    )  
  
#### Parameters

 _processClass_
    The class of the process, e.g. "Drive Dimensions", useful for filtering.
_processTarget_
    The target of the process, e.g. "SomePart.sldprt", useful for filtering.
_processDescription_
    The human-readable description of the process, e.g. "Driving dimensions in part 'SomePart.sldprt'".

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProxyReportWriter Class](topic10434.md)   
[ProxyReportWriter Members](topic10435.md)   
[Overload List](topic10443.md)


