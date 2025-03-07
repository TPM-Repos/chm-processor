Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CompositeReportWriter Constructor(IEnumerable<IReportWriter>)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [CompositeReportWriter Class](topic10363.md) > [CompositeReportWriter Constructor](topic10369.md) : CompositeReportWriter Constructor(IEnumerable<IReportWriter>)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writers_
    The report writers to compose into a single report writer.

Glossary Item Box

Initializes a new instance of the [CompositeReportWriter](topic10363.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _writers_ As IEnumerable(Of IReportWriter) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim writers As IEnumerable(Of IReportWriter)
     
    Dim instance As New [CompositeReportWriter](topic10363.md)(writers)  
  
C#|   
---|---  
      
    
    public CompositeReportWriter( 
       IEnumerable<IReportWriter> _writers_
    )  
  
#### Parameters

 _writers_
    The report writers to compose into a single report writer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CompositeReportWriter Class](topic10363.md)   
[CompositeReportWriter Members](topic10364.md)   
[Overload List](topic10369.md)


