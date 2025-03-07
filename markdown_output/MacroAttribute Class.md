Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MacroAttribute Class   
[Members](topic7226.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) : MacroAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Designates a method on a [ProjectExtender](topic7232.md) as a macro. 

# Object Model

![](dotnetdiagramimages/image390.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Method, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class MacroAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [MacroAttribute](topic7225.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Method, 
       AllowMultiple=false, 
       Inherited=true)]
    public class MacroAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Extensibility.MacroAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[MacroAttribute Members](topic7226.md)   
[DriveWorks.Extensibility Namespace](topic7150.md)


