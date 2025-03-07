Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Fields Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcDataTable Class](topic3746.md) : Fields Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The fields that are used from the selected table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Fields As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcDataTable](topic3746.md)
    Dim value() As String
     
    instance.Fields = value
     
    value = instance.Fields  
  
C#|   
---|---  
      
    
    public string[] Fields {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcDataTable Class](topic3746.md)   
[OdbcDataTable Members](topic3747.md)


