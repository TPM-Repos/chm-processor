Rows Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : Rows Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the rows in the data export document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Rows As [DataExportRowDefinition()](topic2635.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim value() As [DataExportRowDefinition](topic2635.md)
     
    value = instance.Rows  
  
C#|   
---|---  
      
    
    [DataExportRowDefinition[]](topic2635.md) Rows {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


