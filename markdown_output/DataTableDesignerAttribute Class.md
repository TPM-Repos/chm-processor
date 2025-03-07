Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataTableDesignerAttribute Class   
[Members](topic1479.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) : DataTableDesignerAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Applied to a class implementing the [IDataTableDesigner](topic1434.md) interface to provide information about the data table designer. 

# Object Model

![](dotnetdiagramimages/image52.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class DataTableDesignerAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DataTableDesignerAttribute](topic1478.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class DataTableDesignerAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.Administrator.Extensibility.DataTables.DataTableDesignerAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataTableDesignerAttribute Members](topic1479.md)   
[DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md)


