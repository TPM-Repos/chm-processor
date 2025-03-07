Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTableData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ImportedDataTable Class](topic3483.md) : GetTableData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_result_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function GetTableData( _
       ByRef _result_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ImportedDataTable](topic3483.md)
    Dim result As Object
    Dim value As Boolean
     
    value = instance.GetTableData(result)  
  
C#|   
---|---  
      
    
    protected override bool GetTableData( 
       ref Object _result_
    )  
  
#### Parameters

 _result_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ImportedDataTable Class](topic3483.md)   
[ImportedDataTable Members](topic3484.md)


