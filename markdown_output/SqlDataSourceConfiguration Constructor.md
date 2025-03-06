       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SqlDataSourceConfiguration Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [SqlDataSourceConfiguration Class](topic6807.md) : SqlDataSourceConfiguration Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    The XML to use for this configuration.

Glossary Item Box

Creates a new instance of the [SqlDataSourceConfiguration](topic6807.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _data_ As XElement _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim data As XElement
     
    Dim instance As New [SqlDataSourceConfiguration](topic6807.md)(data)  
  
C#|   
---|---  
      
    
    public SqlDataSourceConfiguration( 
       XElement _data_
    )  
  
#### Parameters

 _data_
    The XML to use for this configuration.

# Remarks

The XML will be live edited as properties change in this configuration.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlDataSourceConfiguration Class](topic6807.md)   
[SqlDataSourceConfiguration Members](topic6808.md)


