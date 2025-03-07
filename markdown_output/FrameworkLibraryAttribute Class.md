Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FrameworkLibraryAttribute Class   
[Members](topic7184.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) : FrameworkLibraryAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

For internal use only. Marks an assembly as being part of the DriveWorks core framework. 

# Object Model

![](dotnetdiagramimages/image387.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=False, 
       Inherited=True)>
    <SerializableAttribute()>
    Public Class FrameworkLibraryAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FrameworkLibraryAttribute](topic7183.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=false, 
       Inherited=true)]
    [SerializableAttribute()]
    public class FrameworkLibraryAttribute : System.Attribute   
  
# Remarks

This attribute marks an assembly as being part of the DriveWorks core framework, it will only work when applied to assemblies signed with the DriveWorks private key.

# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Extensibility.FrameworkLibraryAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FrameworkLibraryAttribute Members](topic7184.md)   
[DriveWorks.Extensibility Namespace](topic7150.md)


