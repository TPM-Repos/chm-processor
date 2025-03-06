![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(String,String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10484.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportWriterBase Class](topic10476.md) > [BeginProcess Method](topic10483.md) : BeginProcess(String,String,String) Method  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overridable Sub BeginProcess( _
       ByVal _processClass_ As String, _
       ByVal _processTarget_ As String, _
       ByVal _processDescription_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReportWriterBase](topic10476.md)
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReportWriterBase Class](topic10476.md)   
[ReportWriterBase Members](topic10477.md)   
[Overload List](topic10483.md)

©2024 DriveWorks Ltd. All Rights Reserved.
