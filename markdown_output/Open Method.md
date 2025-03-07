Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Open Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportPackage Class](topic10451.md) : Open Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_filePath_
    The full path to the report package to create.

Glossary Item Box

Opens a new report package. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Open( _
       ByVal _filePath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportPackage](topic10451.md)
    Dim filePath As String
     
    instance.Open(filePath)  
  
C#|   
---|---  
      
    
    public void Open( 
       string _filePath_
    )  
  
#### Parameters

 _filePath_
    The full path to the report package to create.

# Remarks

The report package will be created immediately, any existing file at the specified location will be overwritten.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportPackage Class](topic10451.md)   
[ReportPackage Members](topic10452.md)


