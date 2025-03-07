Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTableData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcDataTable Class](topic3746.md) : GetTableData Method  
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
      
    
    Dim instance As [OdbcDataTable](topic3746.md)
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

[OdbcDataTable Class](topic3746.md)   
[OdbcDataTable Members](topic3747.md)


