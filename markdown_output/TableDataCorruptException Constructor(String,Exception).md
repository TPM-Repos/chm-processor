       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TableDataCorruptException Constructor(String,Exception)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5557.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableDataCorruptException Class](topic5548.md) > [TableDataCorruptException Constructor](topic5554.md) : TableDataCorruptException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    

_inner_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As String
    Dim inner As Exception
     
    Dim instance As New [TableDataCorruptException](topic5548.md)(message, inner)  
  
C#|   
---|---  
      
    
    public TableDataCorruptException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    
_inner_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableDataCorruptException Class](topic5548.md)   
[TableDataCorruptException Members](topic5549.md)   
[Overload List](topic5554.md)

©2024 DriveWorks Ltd. All Rights Reserved.
