Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LibraryAttribute Class   
[Members](topic7202.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) : LibraryAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Marks an assembly as being a DriveWorks extension library. 

# Object Model

![](dotnetdiagramimages/image389.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=False, 
       Inherited=True)>
    <SerializableAttribute()>
    Public NotInheritable Class LibraryAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [LibraryAttribute](topic7201.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=false, 
       Inherited=true)]
    [SerializableAttribute()]
    public sealed class LibraryAttribute : System.Attribute   
  
# Remarks

The publisher name is taken from the System.Reflection.AssemblyCompanyAttribute which is generally defined in an AssemblyInfo.vb or AssemblyInfo.cs file and available from a project's properties.

# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Extensibility.LibraryAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Members](topic7202.md)   
[DriveWorks.Extensibility Namespace](topic7150.md)


