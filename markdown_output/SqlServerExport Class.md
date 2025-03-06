SqlServerExport Class   
[Members](topic5418.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : SqlServerExport Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides support for exporting data to an SQl Server database as part of a DriveWorks specification. 

# Object Model

![](dotnetdiagramimages/image273.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Class SqlServerExport 
       Inherits [ProjectDocument](topic4356.md)
       Implements [DriveWorks.Extensibility.IExtension](topic7152.md), [IDataExportDefinition](topic2177.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)  
  
C#|   
---|---  
      
    
    public class SqlServerExport : [ProjectDocument](topic4356.md), [DriveWorks.Extensibility.IExtension](topic7152.md), [IDataExportDefinition](topic2177.md)    
  
# Remarks

To create a new instance of an SqlServerDataExport document, use the [Project](topic4395.md).[Documents](topic4434.md).[CreateDocument](topic4442.md) method.

# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.ProjectDocument](topic4356.md)  
**DriveWorks.SqlServerExport**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Members](topic5418.md)   
[DriveWorks Namespace](topic2159.md)


