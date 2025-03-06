![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ProcessEventArgs Class](topic10424.md) : ProcessEventArgs Constructor  
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

Initializes a new instance of the [ProcessEventArgs](topic10424.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _processClass_ As String, _
       ByVal _processTarget_ As String, _
       ByVal _processDescription_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim processClass As String
    Dim processTarget As String
    Dim processDescription As String
     
    Dim instance As New [ProcessEventArgs](topic10424.md)(processClass, processTarget, processDescription)  
  
C#|   
---|---  
      
    
    public ProcessEventArgs( 
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

[ProcessEventArgs Class](topic10424.md)   
[ProcessEventArgs Members](topic10425.md)


