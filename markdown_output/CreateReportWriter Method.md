Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateReportWriter Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [IReportWriterFactory Interface](topic10355.md) : CreateReportWriter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    

Glossary Item Box

Creates a new report writer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateReportWriter( _
       ByVal _title_ As String _
    ) As [IReportWriter](topic10344.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReportWriterFactory](topic10355.md)
    Dim title As String
    Dim value As [IReportWriter](topic10344.md)
     
    value = instance.CreateReportWriter(title)  
  
C#|   
---|---  
      
    
    [IReportWriter](topic10344.md) CreateReportWriter( 
       string _title_
    )  
  
#### Parameters

 _title_
    

#### Return Value

The newly created report writer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReportWriterFactory Interface](topic10355.md)   
[IReportWriterFactory Members](topic10356.md)


